# Karlsruhe RAG Assistant :

A Retrieval-Augmented Generation (RAG) system that provides information about locations in Karlsruhe, Germany, using OpenStreetMap data and LlamaIndex.

# Features :

Data Ingestion: Fetches real-time location data (restaurants, cafes, attractions) from OpenStreetMap.

Vector Search: Uses Milvus for efficient similarity search of location metadata.

Intelligent Q&A: Uses the Mistral model via Ollama to generate context-aware answers.

# Prerequisites :

Python 3.11+

Ollama with mistral:7b-instruct-v0.3-q4_0 model pulled.

Milvus (Lite) installed via requirements.txt.

Installation :

# Clone the repository

git clone <your-repo-url>
cd karlsruhe-rag

# Setup virtual environment

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Usage

To ask a question about Karlsruhe:
python src/query.py "Your question here"

# Example Queries and Results 

Query: "I am looking for the best sushi restaurant in Europaplatz."
Retrieved Context:
Source 1: Sushi Park is a restaurant in Karlsruhe, located at latitude 49.0032801 and longitude 8.4226593.
Source 2: Sushi-Palace is a restaurant in Karlsruhe, located at latitude 49.0053277 and longitude 8.3811431.
Source 3: ON Sushi is a restaurant in Karlsruhe, located at latitude 49.0114852 and longitude 8.3610409.
Final Response: There isn't any specific information about a sushi restaurant located in Europaplatz within the given context. To find the best sushi restaurant in Europaplatz, you may want to explore further or consult other sources.
Visualization: View on Google Maps

Query: "Where can I bring my 2 kids to visit in Karlsruhe?"
Retrieved Context:
Source 1: Schlossgartenbahn is a attraction in Karlsruhe, located at latitude 49.0142372 and longitude 8.4010380.
Source 2: Karlsruher Hof is a restaurant in Karlsruhe, located at latitude 49.0053102 and longitude 8.3335171.
Source 3: Unnamed Place is a attraction in Karlsruhe, located at latitude 49.0007908 and longitude 8.3230515.
Final Response: In Karlsruhe, you can consider visiting a few attractions that might interest your kids. One option is the Schlossgartenbahn, another is the Unnamed Place, and for a meal, the Karlsruher Hof restaurant could be a great choice.
Visualization: View on Google Maps

Query: "I want to buy a new washing machine and where can I go to check in the city?"
Retrieved Context:
Source 1: REWE City is a supermarket in Karlsruhe, located at latitude 49.0099674 and longitude 8.3923058.
Source 2: Asia Store is a supermarket in Karlsruhe, located at latitude 49.0075478 and longitude 8.4109093.
Source 3: Kliver City Park is a supermarket in Karlsruhe, located at latitude 49.0019566 and longitude 8.4159555.
Final Response: In the city you're in, you can visit any of the supermarkets that may carry washing machines. Options include REWE City, Asia Store, or Kliver City Park. To confirm if they have the appliance you're looking for, it would be best to contact them or visit their store directly.
Visualization: View on Google Maps

Query: "What are some popular tourist attractions I can visit in Karlsruhe?"
Retrieved Context:
Source 1: Unnamed Place is a attraction in Karlsruhe, located at latitude 49.0007908 and longitude 8.3230515.
Source 2: Schlossgartenbahn is a attraction in Karlsruhe, located at latitude 49.0142372 and longitude 8.4010380.
Source 3: Onager is a attraction in Karlsruhe, located at latitude 48.9911503 and longitude 8.4200300.
Final Response: In Karlsruhe, there are several attractions that you might find interesting: Unnamed Place, Schlossgartenbahn, and Onager.
Visualization: View on Google Maps

Query: "I need a place to grab a coffee in the city, any suggestions?"
Retrieved Context:
Source 1: Good Karma Coffee is a cafe in Karlsruhe, located at latitude 48.9717424 and longitude 8.4675294.
Source 2: Coffee Boxx is a cafe in Karlsruhe, located at latitude 49.0149466 and longitude 8.3842480.
Source 3: Coffee Boxx is a restaurant in Karlsruhe, located at latitude 49.0149687 and longitude 8.3844958.
Final Response: In Karlsruhe, you might want to consider visiting Good Karma Coffee or Coffee Boxx, both of which are cafes in the city. Enjoy your coffee!
Visualization: View on Google Maps