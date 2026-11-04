from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 
load_dotenv()

model =ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_CHAT_MODEL"),
    max_tokens = 256
)

print(model.invoke("Write 5 lines on Project AVA:Razer").content[0]['text'])