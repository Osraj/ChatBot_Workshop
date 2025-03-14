"""
Groq Chatbot - Stage 3 Checkpoint

This Checkpoint includes a basic Streamlit UI with Groq API integration.
It's a functional chatbot but without advanced customization options.
"""

import streamlit as st
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Configure the page
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Add a title
st.title("🤖 Groq Chatbot")

# Sidebar with basic information
with st.sidebar:
    st.header("About")
    st.write("This is a basic chatbot using the Groq API.")
    st.write("More customization options will be added in the next stage.")
    
    # Add a button to reset the conversation
    if st.button("Reset Conversation"):
        # Clear the chat history, preserving system prompt if it exists
        if "messages" in st.session_state and len(st.session_state.messages) > 0:
            if st.session_state.messages[0]["role"] == "system":
                system_prompt = st.session_state.messages[0]
                st.session_state.messages = [system_prompt]
            else:
                st.session_state.messages = []
        else:
            st.session_state.messages = []
        st.rerun()

# Initialize Groq client
try:
    client = groq.Client(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {str(e)}")
    if not api_key:
        st.error("API key not found. Please add your Groq API key to the .env file.")
    st.stop()

# Add a system prompt for the chatbot
system_prompt = "You are a helpful assistant."

# Initialize chat message history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
elif len(st.session_state.messages) == 0:
    # Add system prompt if messages list is empty
    st.session_state.messages.append({"role": "system", "content": system_prompt})
elif st.session_state.messages[0]["role"] != "system":
    # Add system prompt if first message is not a system message
    st.session_state.messages.insert(0, {"role": "system", "content": system_prompt})

# Display existing chat messages (excluding system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system prompt
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input for user
user_input = st.chat_input("Type your message here...")

# Process user input (when provided)
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Display a spinner while waiting for API response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking..."):
            try:
                # Call Groq API
                response = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model="llama3-8b-8192",  # Default model
                    temperature=0.7,         # Default temperature
                    max_tokens=1024          # Default response length
                )
                
                # Extract assistant response
                assistant_response = response.choices[0].message.content
                
                # Display the response
                message_placeholder.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
            except Exception as e:
                # Display error message
                error_message = f"Error: {str(e)}"
                message_placeholder.error(error_message)
                
                # Provide more helpful error messages
                if "API key" in str(e).lower():
                    st.sidebar.error("⚠️ API key error. Check your .env file.")
                elif "rate limit" in str(e).lower():
                    st.sidebar.error("⚠️ Rate limit exceeded. Try again later.")
                else:
                    st.sidebar.error(f"⚠️ An error occurred: {str(e)}")

# Add a footer
st.divider()
st.caption("Created in the Groq Chatbot Workshop")