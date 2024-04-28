import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_templates = {
    'formal': """
        You are an expert at crafting formal self-introductions.
        Please generate a self-introduction that is professional and reserved.
    """,
    'casual': """
        You are an expert at crafting casual self-introductions.
        Please generate a self-introduction that is friendly and informal.
    """,
    'enthusiastic': """
        You are an expert at crafting enthusiastic self-introductions.
        Please generate a self-introduction that is lively and engaging.
    """,
    'professional': """
        You are an expert at crafting professional self-introductions.
        Please generate a self-introduction that balances formality with personal touch.
    """
}

def generate_content(prompt, tone):
    prompt_template = prompt_templates[tone] + "\n\nThe user's details are:\n{prompt}"
    full_prompt = prompt_template.format(prompt=prompt)
    response = model.generate_content(full_prompt)
    return response.text

st.title("🏝️ AI Self-Introduction Generator")

# User inputs
prompt = st.text_area("Enter your name, profession, interests, and a fun fact about yourself:")
tone = st.selectbox("Choose the tone for your introduction:", options=['formal', 'casual', 'enthusiastic', 'professional'])

# Button to generate introduction
if st.button("Generate My Introduction"):
    reply = generate_content(prompt, tone)
    st.write(reply)