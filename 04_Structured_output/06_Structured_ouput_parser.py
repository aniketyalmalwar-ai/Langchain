from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
)

response_schema = [
    ResponseSchema(
        name="name",
        description="Full name of the person"
    ),
    ResponseSchema(
        name="age",
        description="Current age of the person"
    ),
    ResponseSchema(
        name="birth_year",
        description="Year of birth"
    ),
    ResponseSchema(
        name="latest_movies",
        description="List of latest movie names",
        type="List[string]"
    )
]

parser = StructuredOutputParser.from_response_schemas(
    response_schema
)

template = PromptTemplate(
    template="Provide me details of the {name}, like name, age, birth year, and a list of latest movie names. {format_instructions}",
    input_variables=['name'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)
prompt = template.format(name="Allu Arjun")

result = model.invoke(prompt)
final_result = parser.parse(result.content[0]['text'])
print(final_result)
print(type(final_result))

print(result)
