import streamlit as st
from main import *

st.title("Tara")
st.subheader("Introducing a low code and robust semantic NLP engine")

st.info("Tara is a low resource consuming NLP engine that let's you perform various NLP tasks such as summarisation,  NER, Q&A, Topic modelling and Word embedding and much more")


if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Streamlit's open-source Python library!"}
    ]

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])


# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = abstracts(prompt)
            st.write(response)
            message = {"role": "assistant", "content": response[:200]}
            st.session_state.messages.append(message) # Add response to message history
