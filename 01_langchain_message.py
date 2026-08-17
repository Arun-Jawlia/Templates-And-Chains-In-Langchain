from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages = [SystemMessage(content='''You are an Helpful assistant and been helping Youtuber grow their page since last 3 years'''),
HumanMessage(content='''As a Youtuber help me grow my content of selling AI Art in less than 50 words''')
]

model = ChatOpenAI(model='gpt-4o')

response = model.invoke(messages)

print(AIMessage(response.content))

# print(response)