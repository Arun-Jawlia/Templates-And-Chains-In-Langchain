#pylint: disable = all
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

load_dotenv()

st.title("RGC Prompt Template ChatBot")

role = st.selectbox("Select your Role: ", ['AI Engineer', 'Data Scientist', 'Data Engineer', 'Data Analyist'])
goal = st.text_input("What goal you have in mind")
context = st.text_area("Tell me about your experience")

# template = PromptTemplate(
#     template= """v You are and senior {role} working in a company. You always have a {goal} in mind and you have {context} """, 
#     input_variables = ['role', 'goal', 'context'],
#     validate_template = True
#     )    


template = load_prompt('prompt.json')

prompt = template.invoke({'role':role, 'goal':goal, 'context':context})

model = ChatOpenAI(model ='gpt-3.5-turbo')
response = model.invoke(prompt)

if st.button("Answer me"):
    st.write(response.content)