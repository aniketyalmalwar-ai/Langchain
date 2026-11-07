from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite'
)

template = PromptTemplate(
    template="write essay on the {topic}",
    input_variables=['topic']
)
template2 = PromptTemplate(
    template = "Rate the essay from 1 to 10 based on topic coverage, depth of meaning, relevance, clarity, and completeness./n{text}",
    input_variables=['text']
)
parser = StrOutputParser()

chain = template | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Langchain Chains'})

print(result)
chain.get_graph().print_ascii()