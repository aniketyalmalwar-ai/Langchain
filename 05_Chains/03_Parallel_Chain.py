from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite'
)

model2 = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

template = PromptTemplate(
    template="write essay on the {topic}",
    input_variables=['topic']
)
template2 = PromptTemplate(
    template="Evaluate the essay from 1 to 10 based on topic coverage, depth, relevance, clarity, and completeness. Provide a score with justification. Essay: {text}", 
    input_variables=["text"]
)

template3 = PromptTemplate(
    template="Analyze the essay and identify its three major strengths, three weaknesses, and specific improvement suggestions. Essay: {text}", 
    input_variables=["text"]
)
parser = StrOutputParser()

essay_chain = template | model2 | parser

parallel_chain = RunnableParallel({
    "Rating_current_essay": template2 | model1 | parser,
    "suggestions_on_essay": template3 | model2 | parser
    
})


chain = essay_chain | parallel_chain

result = chain.invoke("Narendra Modi")

print(result)

chain.get_graph().print_ascii()