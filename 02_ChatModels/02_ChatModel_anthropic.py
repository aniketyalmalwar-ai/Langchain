
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-sonnet-5-5",
    max_retries=3,
    max_tokens=1024
)

response = model.invoke(
    "Write 5 lines about Project AVA: Razer."
)

print(response.content)
