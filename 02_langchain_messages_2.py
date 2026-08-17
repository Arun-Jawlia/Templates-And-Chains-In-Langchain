from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

domain = input("Domain: ")
query = input("Query: ")


messages = ChatPromptTemplate.from_messages([("system", '''You are an expert {domain} and have been helping people since last 3 years'''), (
    'human', 'Help me with explaining {query} in less than 50 words'
)])

prompt = messages.invoke({'domain':domain, 'query': query})

model = ChatOpenAI(model='gpt-3.5-turbo')

response = model.invoke(prompt)

print(response.content)