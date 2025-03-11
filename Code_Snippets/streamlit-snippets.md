# Streamlit Code Snippets

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)

Ready-to-use Streamlit code snippets for your chatbot project.

## Table of Contents
- [Streamlit Code Snippets](#streamlit-code-snippets)
  - [Table of Contents](#table-of-contents)
  - [Basic App Structure](#basic-app-structure)
  - [Chat Interface](#chat-interface)
  - [Sidebar Controls](#sidebar-controls)
  - [Session State](#session-state)
  - [Error Handling](#error-handling)

## Basic App Structure

```python
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Custom Chatbot",
    page_icon="🤖",
    layout="wide"
)

# App title
st.title("🤖 Custom Chatbot with Groq API")

# Main content area
st.write("Welcome to the chatbot workshop!")

# Footer
st.markdown("---")
st.caption("Created during the Chatbot Workshop")
```

## Chat Interface

```python
# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_input = st.chat_input("Ask something...")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Display assistant response (placeholder)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Replace this with actual API call
        assistant_response = "This is a placeholder response."
        
        # Display the response
        message_placeholder.markdown(assistant_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
```

## Sidebar Controls

```python
# Sidebar title
st.sidebar.title("Customize Your Chatbot")

# Model selection
model_options = {
    "Llama 3 8B": "llama3-8b-8192",
    "Llama 3 70B": "llama3-70b-8192",
    "Mixtral 8x7B": "mixtral-8x7b-32768",
    "Gemma 7B": "gemma-7b-it"
}
selected_model = st.sidebar.selectbox("Select Model", list(model_options.keys()))
model = model_options[selected_model]

# Temperature setting
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
st.sidebar.caption("Higher values make output more random, lower values more deterministic")

# Response length
max_tokens = st.sidebar.slider("Response Length", min_value=50, max_value=4096, value=1024, step=50)

# Add a reset button
if st.sidebar.button("Reset Conversation"):
    st.session_state.messages = []
    st.rerun()
```

## Session State

```python
# Initialize session variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "settings" not in st.session_state:
    st.session_state.settings = {
        "model": "llama3-8b-8192",
        "temperature": 0.7,
        "max_tokens": 1024
    }

# Update settings
def update_settings():
    st.session_state.settings["model"] = model
    st.session_state.settings["temperature"] = temperature
    st.session_state.settings["max_tokens"] = max_tokens

# Apply settings button
if st.sidebar.button("Apply Settings"):
    update_settings()
    st.sidebar.success("Settings applied!")
```

## Error Handling

```python
# Display assistant response with error handling
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    
    try:
        # Call API (replace with actual API call)
        assistant_response = "This is a mock response."
        
        # Display the response
        message_placeholder.markdown(assistant_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    except Exception as e:
        error_message = f"Error: {str(e)}"
        message_placeholder.error(error_message)
        
        # Provide help based on error type
        if "API key" in str(e).lower():
            st.sidebar.warning("⚠️ API key error. Check your .env file.")
        elif "rate limit" in str(e).lower():
            st.sidebar.warning("⚠️ Rate limit exceeded. Try again later.")
        else:
            st.sidebar.warning(f"⚠️ An error occurred: {str(e)}")
```

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)