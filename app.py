import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are an expert at crafting engaging self-introductions.

Please generate a self-introduction based on the following details provided by the user:
- Name
- Profession
- Interests
- A fun fact about them

The user's detail is:
{prompt}
"""

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title("🏝️ AI Travel Planning")

prompt = st.text_area("Enter your next travel request (days, destination, activities, etc.):")
if st.button("Give me a plan!"):
    reply = generate_content(prompt)
    st.write(reply)