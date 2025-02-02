# Import necessary libraries
import streamlit as st
import openai

# Set up your OpenAI API key
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')


# Initialize Streamlit
st.title("Ask GPT-3 a question")

# Create a text input field for user queries
user_input = st.text_input("Ask a question:")

#Create temperature slider
temperature = st.slider("Temperature", 0.1, 1.0, 0.7)

# Send the user's query to OpenAI GPT-3
if user_input:
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=user_input,
    max_tokens=50
    )
    st.write(response['choices'][0]['text'].strip())
