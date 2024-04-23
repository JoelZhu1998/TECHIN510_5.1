import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key = 'GOOGLE_API_KEY')

model = genai.GenerativeModel('gemini-pro')

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title('Gemini Playground')

prompt = st.text_area("Enter your prompt")
if st.button("Give me a plan!"):
    reply = generate_content(prompt)
    st.write(reply)