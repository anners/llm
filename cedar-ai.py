import openai
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI()
chat_model = ChatOpenAI()

prompt = input("Send a message: ")

print(llm(prompt))
