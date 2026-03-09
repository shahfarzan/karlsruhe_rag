import overpy
import time
from llama_index.core import Document, VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 1. Setup Models
Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Fetch data from OpenStreetMap with a retry mechanism
api = overpy.Overpass()
query = """
[out:json][timeout:60];
area["name"="Karlsruhe"]->.searchArea;
(
  node["amenity"~"restaurant|cafe"](area.searchArea);
  node["shop"~"supermarket|mall"](area.searchArea);
  node["tourism"~"attraction"](area.searchArea);
);
out body;
"""

print("Fetching data from OpenStreetMap...")
max_retries = 3
result = None
for i in range(max_retries):
    try:
        result = api.query(query)
        print(f"Success! Found {len(result.nodes)} places.")
        break
    except overpy.exception.OverpassGatewayTimeout:
        print(f"Server busy, retrying in {i+1} seconds...")
        time.sleep(i + 1)

if not result:
    print("Failed to reach OSM server. Please try again later.")
    exit()

# 3. Create Documents with Metadata
documents = []
for node in result.nodes:
    name = node.tags.get("name", "Unnamed Place")
    category = node.tags.get("amenity") or node.tags.get("shop") or node.tags.get("tourism")
    lat, lon = node.lat, node.lon
    
    text = f"{name} is a {category} in Karlsruhe, located at latitude {lat} and longitude {lon}."
    
    doc = Document(
        text=text,
        metadata={"name": name, "type": category, "lat": float(lat), "lon": float(lon)}
    )
    documents.append(doc)

# 4. Split documents into chunks
parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
nodes = parser.get_nodes_from_documents(documents)

# 5. Connect to Milvus and store
vector_store = MilvusVectorStore(
    uri="./milvus_karlsruhe.db", 
    dim=384, 
    overwrite=True 
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(nodes, storage_context=storage_context)

print(f"Successfully ingested {len(nodes)} chunks into Milvus.")