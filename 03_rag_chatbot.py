from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
data = SimpleDirectoryReader(input_dir="pdf/").load_data()
index = VectorStoreIndex.from_documents(data)


chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

while True:
    text_input = input("User: ")
    if text_input == "exit":
        break
    response = chat_engine.chat(text_input)
    print(f"Agent: {response}")