from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite'
)

template = PromptTemplate(
    template="write short information on the {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({'topic':'Langchain Chains'})

print(result)
chain.get_graph().print_ascii()