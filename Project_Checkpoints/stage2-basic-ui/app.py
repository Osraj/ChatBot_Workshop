"""
Groq Chatbot - Stage 2 Checkpoint

This Checkpoint includes a basic Streamlit UI for the chatbot,
but does not yet have any API integration.
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables (for later use)
load_dotenv()

# Configure the page
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Add a title
st.title("🤖 Groq Chatbot")

# Sidebar with placeholder for future controls
with st.sidebar:
    st.header("Settings")
    st.write("Customization options will be added here in future stages.")
    
    # Add a button to reset the conversation
    if st.button("Reset Conversation"):
        # This will be implemented to clear the chat history
        st.write("Reset functionality will be implemented later.")

# Initialize chat message history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
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
    
    # In this Checkpoint, we'll just echo the user's message as a placeholder
    # In later stages, this will be replaced with actual API calls
    placeholder_response = f"You said: '{user_input}'\n\n(This is just a placeholder response. API integration will be added in the next stage.)"
    
    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(placeholder_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": placeholder_response})

# Add a footer
st.divider()
st.caption("Created in the Groq Chatbot Workshop")