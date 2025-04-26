import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.openai import OpenAI  
import chromadb

load_dotenv()

# 1. Load data
documents = SimpleDirectoryReader("pdf/").load_data()

# 2. Initialize ChromaDB
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 3. Define the OpenAI LLM explicitly
llm = OpenAI(
    model="gpt-3.5-turbo",  
    temperature=0.1,        
    max_tokens=512,         
)

# 4. Create the index with the LLM
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    llm=llm,  # Attach the LLM to the index
)

# 5. Query with the LLM
query_engine = index.as_query_engine(llm=llm)  # Use the same LLM for queries
response = query_engine.query("What are the design goals and give details about it please.")
print("***********")
print(response)