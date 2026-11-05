from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
)

class Artist(BaseModel):
    name :str =Field(description="Name of the actor")
    age : int =Field(gt=0,description="Age of the Actor")
    residence:str = Field(description="The country name of which actor is residence")

parser = PydanticOutputParser(pydantic_object=Artist)

template = PromptTemplate(
    template="Provide me the name , age and country of residence of the ramdom actor/actress. {format_instructions}",
    input_variables=[],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)
prompt = template.format()
print(prompt)

result = model.invoke(prompt)
final_result = parser.parse(result.content[0]['text'])

print(final_result)
print(type(final_result))

print(final_result.model_dump_json())
