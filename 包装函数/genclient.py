
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        api_key=os.getenv("api_key"),
        base_url = os.getenv("base_url")
)

def genclient(messages,model,tools):
    return client.chat.completions.create(
        model = model,
        messages = messages,
        tools = tools
    )
