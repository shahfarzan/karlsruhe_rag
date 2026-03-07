import argparse
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

def main():
    # 1. Setup CLI arguments
    parser = argparse.ArgumentParser(description="Karlsruhe RAG Query Engine")
    parser.add_argument("question", type=str, help="The question you want to ask about Karlsruhe")
    args = parser.parse_args()

    # 2. Setup Models
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    Settings.llm = Ollama(
        model="mistral:7b-instruct-v0.3-q4_0", 
        request_timeout=1000.0
    )

    # 3. Connect to existing Milvus database
    vector_store = MilvusVectorStore(
        uri="./milvus_karlsruhe.db", 
        dim=384, 
        overwrite=False
    )

    # 4. Load the index
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context)

    # 5. Run the query
    query_engine = index.as_query_engine(similarity_top_k=3)
    response = query_engine.query(args.question)

    print("\n--- Final Intelligent Response ---")
    print(response)

if __name__ == "__main__":
    main()