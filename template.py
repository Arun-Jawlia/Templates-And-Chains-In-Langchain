from langchain_core.prompts import PromptTemplate
import streamlit as st

role = st.selectbox("Select your Role: ", ['AI Engineer', 'Data Scientist', 'Data Engineer', 'Data Analyist'])
goal = st.text_input("What goal you have in mind")
context = st.text_area("Tell me about your experience")

template = PromptTemplate(
    template= """v You are and senior {role} working in a company. You always have a {goal} in mind and you have {context} """, 
    input_variables = ['role', 'goal', 'context'],
    validate_template = True
    )    

template.save('prompt.json')