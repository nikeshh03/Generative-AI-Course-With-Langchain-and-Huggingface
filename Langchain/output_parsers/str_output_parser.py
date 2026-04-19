from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)


template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template="write summary in 5 lines of the given text /n {text}",
    input_variables = ['text']
)

parser = StrOutputParser()

chains = template1 | model | parser | template2 | model | parser

result = chains.invoke({'topic':'Black hole'})

print(result)