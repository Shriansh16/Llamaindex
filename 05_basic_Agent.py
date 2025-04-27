import os
import llama_index.core
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool

from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

def subtract(a: float, b: float) -> float:
    """Subtract two numbers and returns the difference"""
    return a - b

sub_tool = FunctionTool.from_defaults(fn=subtract)

def divide(a: float, b: float) -> float:
    """Divide two numbers and returns the quotient"""
    return a / b

divide_tool = FunctionTool.from_defaults(fn=divide)


agent = ReActAgent.from_tools([multiply_tool, add_tool, sub_tool, divide_tool], llm=llm, verbose=True)

response = agent.chat("What is 20+(2*4) / (5 - 1)? Use a tool to calculate every step.")        

print(response)