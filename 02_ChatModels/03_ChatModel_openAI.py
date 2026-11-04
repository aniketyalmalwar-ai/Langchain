
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-6.1-terra",
    max_retries=3,
    max_tokens=512
)

response = model.invoke(
    "Write 5 lines about Project AVA: Razer."
)

print(response.content)
