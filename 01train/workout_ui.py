from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os 
load_dotenv()

import streamlit as st
from langchain_core.prompts import load_prompt

model =ChatHuggingFace(llm=HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-20b",
        task="text-generation",
        temperature=0,
        max_new_tokens=1024,
        huggingfacehub_api_token=os.getenv("HUGGINFACE_API_KEY"))
    )

st.header('workout planning Tool')
name_input = st.text_input("Enter Your Name")
age_input = st.text_input("Enter Your Age")
weight_input = st.text_input("Enter Your Weight (in kg)")
height_input = st.text_input("Enter Your Height (in cm)")
medical_conditions_input = st.text_area("Enter Any Medical Conditions (if any)")
fitness_goals_input = st.text_area("Enter Your Fitness Goals")  


template = load_prompt('template_medical_workout.json')



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        "age": age_input,
        "fitness_goals": fitness_goals_input,
        "height": height_input,
        "medical_conditions": medical_conditions_input,
        "name": name_input,
        "weight": weight_input
    })
    st.write(result.content)