import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# configure gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-3.5-flash")

# page layout
st.set_page_config(page_title="AI ChatBOT",page_icon="🧊",layout="centered")

# Title
st.title("AI ChatBOT")
st.write("Chat with Gemini")

# session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
user_input = st.chat_input("Type your question...")

if user_input:

    # display user input
    st.chat_message("user").markdown(user_input)

    # save user input
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    # generate ai response
    response = model.generate_content(user_input)
    ai_response = response.text

    # display ai response
    st.chat_message("assistant").markdown(ai_response)

    # save ai response
    st.session_state.messages.append({
        "role":"assistant",
        "content":ai_response
    })