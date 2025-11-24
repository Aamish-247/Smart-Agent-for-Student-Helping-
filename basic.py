from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
load_dotenv()
import os

api_key = os.getenv("Groq_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b", api_key= api_key)

response = model.invoke("who are you?")

print(response.content)

print(type(response))