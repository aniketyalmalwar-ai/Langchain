from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal
load_dotenv()

cust_review = "Excellent mobile phone! The performance is smooth, the display quality is great, and the design looks premium. Battery life and overall features are impressive. Good value for money. Highly recommended!" 

class Review(TypedDict):
    summary :Annotated[str,"A short summary of the customer review."]
    sentiment:Annotated[Literal["Pos","Neg"],"Return sentiment of the review either negative or positive."]

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite'
)

structured_model = model.with_structured_output(Review)
result = structured_model.invoke(cust_review)
print(result["summary"])
print(result["sentiment"])