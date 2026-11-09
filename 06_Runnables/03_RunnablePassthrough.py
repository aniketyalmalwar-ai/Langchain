from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel
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

generate_joke = RunnableSequence(prompt,model,parser)
parallel_runnable = RunnableParallel({
    "Joke" :RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)

})
chain = RunnableSequence(generate_joke,parallel_runnable)
print((chain.invoke({'topic':'Politics'})))