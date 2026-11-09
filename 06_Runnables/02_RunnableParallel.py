from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

prompt = PromptTemplate(
    template="Write linkdin post for {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="give tweet for topic {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_runnable = RunnableParallel({
    "Linkdin post": RunnableSequence(prompt,model,parser),
    "tweet": RunnableSequence(prompt2,model,parser)
})

result = parallel_runnable.invoke({'topic':'Politics'})
print(result['Linkdin post'])
print("_"*100)
print(result['tweet'])