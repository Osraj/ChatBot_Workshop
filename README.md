# Customized Chatbot Workshop

A 2-day workshop to build a customized chatbot using Groq API and Streamlit.

## Workshop Overview

- **Total Duration:** 4 hours (2 hours per day)
- **Format:** Online
- **Final Project:** Customized chatbot with Groq API and Streamlit

## Quick Links

- [📋 All Cheat Sheets](Cheat_Sheets/README.md)
- [📊 System Architecture](Diagrams/architecture.md)
- [💻 Code Snippets](Code_Snippets/README.md)
- [🚀 Project Templates](Project_Templates/README.md)

## Prerequisites

Participants should have:
- Basic understanding of programming concepts
- Computer with internet connection
- Admin rights to install software on their machine

## Workshop Schedule

### Day 1: Environment Setup and Python Basics (2 hours)

#### 1. Environment Setup (30 minutes)
- Installing Miniconda
- Setting up VSCode
- Creating a virtual environment
- Installing required packages

#### 2. Python Basics Review (30 minutes)
- Variables, data types, and functions
- Working with dictionaries and lists
- Understanding API concepts

#### 3. Introduction to Groq API (60 minutes)
- What is Groq and LLM API
- Setting up Groq API account and getting API keys
- Making basic API calls
- Understanding response structure

### Day 2: Building the Chatbot (2 hours)

#### 1. Introduction to Streamlit (30 minutes)
- What is Streamlit
- Basic Streamlit components
- Creating simple Streamlit apps

#### 2. Building the Chatbot UI (45 minutes)
- Designing the chat interface
- Managing chat history
- Connecting to Groq API

#### 3. Customization Options (30 minutes)
- Adding model selection
- Implementing temperature control
- Creating persona selection
- Adding system prompts

#### 4. Testing and Deployment (15 minutes)
- Testing the chatbot
- Troubleshooting
- Sharing the app

## System Architecture

![Chatbot Architecture](Diagrams/architecture-thumbnail.png)

The chatbot we'll build follows this architecture:
1. **User Interface**: Streamlit web app
2. **Business Logic**: Python backend
3. **AI Service**: Groq API integration
4. **Customization**: Model selection, personas, and parameters

[View Full Architecture Diagram](Diagrams/architecture.md)

## Detailed Setup Instructions

### Installing Miniconda

1. Download Miniconda:
   - **Windows**: [Miniconda Windows Installer](https://docs.conda.io/en/latest/miniconda.html)
   - **macOS**: [Miniconda macOS Installer](https://docs.conda.io/en/latest/miniconda.html)
   - **Linux**: [Miniconda Linux Installer](https://docs.conda.io/en/latest/miniconda.html)

2. Install Miniconda:
   - **Windows**: Double-click the installer and follow the instructions
   - **macOS**: Run `bash Miniconda3-latest-MacOSX-x86_64.sh` in Terminal
   - **Linux**: Run `bash Miniconda3-latest-Linux-x86_64.sh` in Terminal

3. Verify installation:
   ```bash
   conda --version
   ```

### Installing Visual Studio Code

1. Download VS Code:
   - Visit [code.visualstudio.com](https://code.visualstudio.com/)
   - Download the appropriate version for your OS

2. Install VS Code:
   - Run the installer and follow the instructions

3. Install Python extensions:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
   - Search for "Python" and install the Microsoft Python extension

### Setting Up the Project Environment

1. Create a new project folder:
   ```bash
   mkdir groq-chatbot
   cd groq-chatbot
   ```

2. Create a new conda environment:
   ```bash
   conda create -n chatbot-env python=3.10
   conda activate chatbot-env
   ```

3. Install required packages:
   ```bash
   pip install streamlit groq python-dotenv
   ```

## Project Structure

Create the following files in your project directory:

```
groq-chatbot/
│
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Project dependencies
├── app.py                # Main Streamlit application
└── README.md             # Project documentation
```

### Contents for requirements.txt

```
streamlit>=1.32.0
groq>=0.4.0
python-dotenv>=1.0.0
```

### Contents for .env

```
GROQ_API_KEY=your_groq_api_key_here
```

## Project Templates

To make it easier to follow along, we've created project templates at different stages:

- [Stage 1: Basic Setup](Project_Templates/stage1-basic-setup) - Environment and dependencies
- [Stage 2: Basic Streamlit UI](Project_Templates/stage2-basic-ui) - Simple UI without API calls
- [Stage 3: Basic Chatbot](Project_Templates/stage3-basic-chatbot) - Chatbot with basic Groq integration
- [Stage 4: Complete Chatbot](Project_Templates/stage4-complete-chatbot) - Fully customized chatbot

If you fall behind during the workshop, you can copy one of these templates to catch up.

## Building the Chatbot

### Step 1: Setting Up the Environment Variables

Create a file named `.env` in your project directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Creating the Customized Chatbot

Create a file named `app.py` with the following code that includes enhanced customization options including character personas and moods:

```python
import streamlit as st
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

# Set page configuration
st.set_page_config(
    page_title="Custom Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Set app title
st.title("🤖 Custom Chatbot with Groq API")

# Sidebar for customization options
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

# Custom system prompt option
use_custom_prompt = st.sidebar.checkbox("Use Custom System Prompt")
if use_custom_prompt:
    system_prompt = st.sidebar.text_area("Enter Custom System Prompt", value=system_prompt, height=100)

# Response style settings
st.sidebar.subheader("Response Settings")
max_tokens = st.sidebar.slider("Response Length", min_value=50, max_value=4096, value=1024, step=50)
emoji_use = st.sidebar.select_slider("Emoji Usage", options=["None", "Minimal", "Moderate", "Abundant"], value="Minimal")

# Add emoji instruction to prompt based on selection
if emoji_use == "None":
    system_prompt += " Do not use any emojis in your responses."
elif emoji_use == "Abundant":
    system_prompt += " Use plenty of relevant emojis throughout your responses."
elif emoji_use == "Moderate":
    system_prompt += " Use some emojis occasionally in your responses."
# No need to add anything for "Minimal" as it's the default

# Add link to cheat sheet
st.sidebar.markdown("---")
st.sidebar.markdown("[📋 Chatbot Customization Cheat Sheet](Cheat_Sheets/README.md)")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
elif st.session_state.messages[0]["role"] == "system":
    # Update system prompt if it changed
    st.session_state.messages[0]["content"] = system_prompt
else:
    # Add system prompt if it doesn't exist
    st.session_state.messages.insert(0, {"role": "system", "content": system_prompt})

# Display chat messages excluding system prompt
for message in st.session_state.messages:
    if message["role"] != "system":
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
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Call Groq API
            response = client.chat.completions.create(
                messages=st.session_state.messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            assistant_response = response.choices[0].message.content
            
            # Display the response
            message_placeholder.markdown(assistant_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        except Exception as e:
            error_message = f"Error: {str(e)}"
            message_placeholder.error(error_message)

# Add a reset button
if st.sidebar.button("Reset Conversation"):
    # Keep the system prompt but clear the conversation
    system_prompt = st.session_state.messages[0]["content"]
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.rerun()

# Display API information
st.sidebar.divider()
st.sidebar.caption(f"Using model: {model}")
if not os.getenv("GROQ_API_KEY"):
    st.sidebar.warning("⚠️ Groq API Key not found. Please add it to your .env file.")
```

## Running the Application

To run the application, activate your environment and use the streamlit command:

```bash
conda activate chatbot-env
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Testing the Project

1. Verify that the chatbot loads correctly in your browser
2. Test basic conversation with the default settings
3. Try different models and observe response differences
4. Adjust temperature and observe changes in creativity/randomness
5. Test different personas and see how responses change
6. Create a custom system prompt for specific use cases
7. Test error handling by temporarily providing an invalid API key

## Troubleshooting

### Common Issues and Solutions

1. **API Key Not Working**
   - Verify that your API key is correct
   - Check that the .env file is in the correct location
   - Ensure the dotenv package is loading correctly

2. **Model Not Responding**
   - Check your internet connection
   - Verify that you haven't exceeded Groq API limits
   - Try a different model

3. **Streamlit App Not Loading**
   - Verify all dependencies are installed
   - Check for syntax errors in your code
   - Restart the Streamlit server

4. **Slow Responses**
   - Larger models take longer to respond
   - Consider using a smaller model for testing
   - Check your internet connection

## Next Steps and Enhancements

After completing the workshop, consider these enhancements:

1. Add file upload capabilities for document Q&A
2. Implement chat history saving and loading
3. Add speech-to-text and text-to-speech features
4. Implement memory management for longer conversations
5. Add RAG (Retrieval-Augmented Generation) capabilities
6. Deploy your chatbot to Streamlit Cloud or other hosting services

## Additional Resources

- [📋 All Cheat Sheets](Cheat_Sheets/README.md)
- [🃏 Quick Reference Cards](Reference_Cards/README.md)
- [💻 Code Snippets](Code_Snippets/README.md)
- [Groq API Documentation](https://console.groq.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Documentation](https://docs.python.org/3/)
- [Conda Documentation](https://docs.conda.io/en/latest/)