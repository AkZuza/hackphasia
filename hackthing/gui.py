import streamlit as st
from main import *
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer=AutoTokenizer.from_pretrained('T5-base')
model=AutoModelWithLMHead.from_pretrained('T5-base', return_dict=True)
st.title("Tara")
st.subheader("Introducing a low code and robust semantic NLP engine")

st.info("Tara is a low resource consuming NLP engine that let's you perform various NLP tasks such as summarisation,  NER, Q&A, Topic modelling and Word embedding and much more")


if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Use me to generate ideas about drones based on around 2.5k drone based patents!"}
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
            sequence = response
            inputs=tokenizer.encode("sumarize: " +sequence,return_tensors='pt', max_length=1024, truncation=True)
            output = model.generate(inputs, min_length=80, max_length=100)
            summary=tokenizer.decode(output[0])
            clean_text = re.sub(r'<[^>]+>', '', summary)
            st.write(clean_text)
            message = {"role": "assistant", "content": clean_text}
            st.session_state.messages.append(message) # Add response to message history




