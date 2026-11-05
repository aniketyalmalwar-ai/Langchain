from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Provide me details of the {name}, like name, age, birth year, and a list of latest movie names. {format_instructions}",
    input_variables=['name'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)
prompt = template.format(name="Allu Arjun")

result = model.invoke(prompt)
final_result = parser.parse(result)
print(final_result)
print(type(final_result))
