from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

def char_counter(text):
    return len(text)

runnable_char_counter = RunnableLambda(char_counter)
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="How many characters contains the  {text}",
    input_variables=['text']
)

parser = StrOutputParser()

generate_joke = RunnableSequence(prompt,model,parser)
parallel_runnable = RunnableParallel({
    "Joke" :RunnablePassthrough(),
    "Total number of characters in joke":runnable_char_counter}) # else you can write as "Total number of characters in joke":RunnableLambda(Lambda x:len(x)
chain = RunnableSequence(generate_joke,parallel_runnable)
print((chain.invoke({'topic':'Politics'})))