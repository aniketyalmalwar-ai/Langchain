
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableSequence,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash-lite',
)

prompt = PromptTemplate(
    template="Write detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the  {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

report_generation = RunnableSequence(prompt,model,parser)
decision_based_branch = RunnableBranch(
    (lambda x:len(x.split())>500 , RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_generation,decision_based_branch)
result = chain.invoke({'topic':'Agentic AI'})
print(result)

chain.get_graph().print_ascii()