from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo")
data = SimpleDirectoryReader("pdf/").load_data()
index = VectorStoreIndex.from_documents(data)

chat_engine = index.as_chat_engine(chat_mode="best", llm=llm, verbose=True)

response = chat_engine.chat(
    "What are the design goals and give details about it please."
)   

print(response)