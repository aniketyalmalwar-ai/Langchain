from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

template = PromptTemplate(
    template="Write deatiled report on {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({"topic":'Project AVA by Razer'})

print(result)