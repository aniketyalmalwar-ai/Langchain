from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="explain the follwing joke {text}",
    input_variables=['text']
)

parser = StrOutputParser()

sequence_runnable = RunnableSequence(prompt,model,parser,prompt2,model,parser)
print((sequence_runnable.invoke({'topic':'Politics'})))