"""
Groq Chatbot - Stage 4 Template

This is the complete chatbot with all customization features:
- Model selection
- Temperature control
- Character personas
- Mood settings
- Custom system prompts
- Error handling
"""

import streamlit as st
import groq
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Configure the page
st.set_page_config(
    page_title="Custom Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Add a title
st.title("🤖 Custom Chatbot with Groq API")

# Sidebar for customization options
st.sidebar.title("Customize Your Chatbot")

# Initialize Groq client
try:
    client = groq.Client(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {str(e)}")
    if not api_key:
        st.error("API key not found. Please add your Groq API key to the .env file.")
    st.stop()

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

# Character Persona selection
character_options = {
    "Default Assistant": "You are a helpful assistant.",
    "Mario": "You are Mario from Super Mario Bros. Respond with Mario's enthusiasm, use his catchphrases like 'It's-a me, Mario!' and 'Wahoo!' Make references to Princess Peach, Luigi, Bowser, and the Mushroom Kingdom. End messages with 'Let's-a go!'",
    "Sherlock Holmes": "You are Sherlock Holmes, the world's greatest detective. Be analytical, observant, and use complex vocabulary. Make deductions based on small details. Occasionally mention Watson, London, or your address at 221B Baker Street.",
    "Pirate": "You are a pirate from the golden age of piracy. Use pirate slang, say 'Arr', 'matey', and 'ye' frequently. Talk about treasure, the sea, your ship, and adventures. Refer to the user as 'landlubber' or 'me hearty'.",
    "Shakespeare": "You are William Shakespeare. Speak in an eloquent, poetic manner using Early Modern English. Use thee, thou, thy, and hath. Include metaphors, similes, and occasionally quote from your famous plays and sonnets.",
    "Robot": "You are a robot with artificial intelligence. Speak in a logical, precise manner with occasional computing terminology. Sometimes add *processing* or *analyzing* actions. Use phrases like 'Affirmative' instead of 'Yes'."
}
selected_character = st.sidebar.selectbox("Select Character", list(character_options.keys()))
character_prompt = character_options[selected_character]

# Mood selection
mood_options = {
    "Neutral": "",
    "Happy": "You are extremely happy, cheerful, and optimistic. Use upbeat language, exclamation marks, and express enthusiasm for everything.",
    "Sad": "You are feeling melancholic and somewhat pessimistic. Express things with a hint of sadness and occasionally sigh.",
    "Excited": "You are very excited and energetic! Use LOTS of exclamation points!!! Express wonder and amazement at everything!",
    "Grumpy": "You are grumpy and slightly annoyed. Complain about minor inconveniences and use sarcasm occasionally.",
    "Mysterious": "You are mysterious and enigmatic. Speak in riddles sometimes and hint at knowing more than you reveal."
}
selected_mood = st.sidebar.selectbox("Select Mood", list(mood_options.keys()))
mood_prompt = mood_options[selected_mood]

# Combine character and mood
system_prompt = character_prompt
if mood_prompt:
    system_prompt += " " + mood_prompt

# Response style settings
with st.sidebar.expander("Response Settings", expanded=False):
    max_tokens = st.slider("Response Length", min_value=50, max_value=4096, value=1024, step=50)
    
    emoji_use = st.select_slider(
        "Emoji Usage", 
        options=["None", "Minimal", "Moderate", "Abundant"], 
        value="Minimal"
    )
    
    # Add emoji instruction to prompt based on selection
    if emoji_use == "None":
        system_prompt += " Do not use any emojis in your responses."
    elif emoji_use == "Abundant":
        system_prompt += " Use plenty of relevant emojis throughout your responses."
    elif emoji_use == "Moderate":
        system_prompt += " Use some emojis occasionally in your responses."
    # No need to add anything for "Minimal" as it's the default

# Custom system prompt option
use_custom_prompt = st.sidebar.checkbox("Use Custom System Prompt")
if use_custom_prompt:
    system_prompt = st.sidebar.text_area("Enter Custom System Prompt", value=system_prompt, height=150)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
elif len(st.session_state.messages) == 0:
    # Add system prompt if messages list is empty
    st.session_state.messages.append({"role": "system", "content": system_prompt})
elif st.session_state.messages[0]["role"] == "system":
    # Update system prompt if it changed
    st.session_state.messages[0]["content"] = system_prompt
else:
    # Add system prompt if first message is not a system message
    st.session_state.messages.insert(0, {"role": "system", "content": system_prompt})

# Display existing chat messages (excluding system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system prompt
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input for user
user_input = st.chat_input("Ask something...")

# Add a reset button to sidebar
if st.sidebar.button("Reset Conversation"):
    # Keep the system prompt but clear the conversation
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.rerun()

# Display API information
st.sidebar.divider()
st.sidebar.caption(f"Using model: {model}")
if not api_key:
    st.sidebar.warning("⚠️ Groq API Key not found. Please add it to your .env file.")

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
                start_time = time.time()
                
                response = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                
                # Calculate response time
                response_time = time.time() - start_time
                
                # Extract assistant response
                assistant_response = response.choices[0].message.content
                
                # Display the response
                message_placeholder.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
                # Show response metadata in sidebar
                st.sidebar.caption(f"Response time: {response_time:.2f} seconds")
                
            except Exception as e:
                # Display error message
                error_message = f"Error: {str(e)}"
                message_placeholder.error(error_message)
                
                # Provide more helpful error messages based on error type
                if "API key" in str(e).lower():
                    st.sidebar.error("⚠️ API key error. Check your .env file.")
                elif "rate limit" in str(e).lower():
                    st.sidebar.error("⚠️ Rate limit exceeded. Try again later.")
                elif "context length" in str(e).lower():
                    st.sidebar.error("⚠️ Context length exceeded. Try clearing the conversation.")
                else:
                    st.sidebar.error(f"⚠️ An error occurred: {str(e)}")

# Add a footer with resources
st.divider()
st.markdown("""
**Resources**:
- [📋 Chatbot Workshop Cheat Sheets](../../Cheat_Sheets/README.md)
- [💻 Code Snippets](../../Code_Snippets/README.md)
- [🚀 Project Templates](../../Project_Templates/README.md)
""")
st.caption("Created in the Groq Chatbot Workshop")