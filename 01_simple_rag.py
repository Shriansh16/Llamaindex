from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
load_dotenv()
OpenAI(model="gpt-3.5-turbo")
documents = SimpleDirectoryReader("pdf/").load_data()

index = VectorStoreIndex.from_documents(documents) 

query_engine = index.as_query_engine()

response = query_engine.query("What are the design goals and give details about it please.")

print(response)