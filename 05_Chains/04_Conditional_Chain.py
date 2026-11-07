
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash-lite',
)

feedback = "Good product but have battery issue"


class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="Give a sentiment of the feedback"
    )


class System_response(BaseModel):
    system: str = Field(
        max_length=250,
        description="System response over the feedback"
    )


parser1 = PydanticOutputParser(pydantic_object=Feedback)
parser2 = PydanticOutputParser(pydantic_object=System_response)


prompt1 = PromptTemplate(
    template="""
    Classify the sentiment of the following feedback text into positive or negative.
    Feedback: {feedback}
    {format_instructions}
    """,
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser1.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser1


prompt2 = PromptTemplate(
    template="""
    Write appropriate response to this positive feedback.
    Feedback: {feedback}
    {format_instructions}
    """,
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

prompt3 = PromptTemplate(
    template="""
    Write appropriate response to this negative feedback.
    Feedback: {feedback}
    {format_instructions}
    """,
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)


conditional_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive",prompt2 | model | parser2),
    (lambda x: x.sentiment == "Negative",prompt3 | model | parser2),
    lambda x: "Could not find sentiment"
)

chain = classifier_chain | conditional_chain

result = chain.invoke({'feedback': feedback})

print(result)

chain.get_graph().print_ascii()
