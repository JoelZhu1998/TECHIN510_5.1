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

User's details:
{prompt}
"""

def generate_content(prompt):
    full_prompt = prompt_template.format(prompt=prompt)
    response = model.generate_content(full_prompt)
    return response.text

st.title("👤 AI Self-Introduction Generator")

user_details = st.text_area("Enter your name, profession, interests, and a fun fact about yourself:")
if st.user_button("Generate My Introduction"):
    introduction = generate_content(user_details)
    st.write(introduction)