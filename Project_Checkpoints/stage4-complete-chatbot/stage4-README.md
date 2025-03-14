# Stage 4: Complete Customized Chatbot

[← Back to Checkpoints](../README.md) | [← Back to Main README](../../README.md)

This is the complete chatbot project with all customization features implemented.

## Contents

- Complete UI with sidebar controls
- Full Groq API integration
- Character personas and moods
- All customization options
- Error handling

## Setup Instructions

1. Make sure you have Python installed (3.8 or higher recommended)

2. Create and activate a conda environment:
   ```bash
   conda create -n chatbot-env python=3.10
   conda activate chatbot-env
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Rename `.env.example` to `.env` and add your API key:
   ```bash
   # On macOS/Linux
   cp .env.example .env
   
   # On Windows
   copy .env.example .env
   ```

5. Open `.env` in a text editor and replace `your_groq_api_key_here` with your actual Groq API key

6. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## What This Checkpoint Includes

- A complete Streamlit UI with:
  - Chat interface
  - Message history
  - User input field
- Groq API integration:
  - Full API calls
  - Error handling
  - Multiple models
- Customization options:
  - Model selection (Llama 3, Mixtral, Gemma)
  - Temperature control
  - Character personas (Mario, Sherlock Holmes, etc.)
  - Mood settings (Happy, Sad, Excited, etc.)
  - Emoji usage control
  - Custom system prompts
  - Response length settings

## Features to Explore

This Checkpoint demonstrates several key concepts:

1. **Session State Management**: Using Streamlit's session state to preserve chat history and settings

2. **Sidebar Controls**: Using the sidebar for customization options

3. **Error Handling**: Proper handling of API errors with helpful messages

4. **System Prompts**: Using system prompts to control the chatbot's behavior

5. **Expandable UI**: UI components that can be expanded for advanced options

## Further Enhancements

Some ideas for enhancing this Checkpoint:

- Add file upload for document Q&A
- Implement chat history saving and loading
- Add speech-to-text capabilities
- Implement streaming responses
- Add memory management for longer conversations
- Deploy to Streamlit Cloud

## File Structure

```
stage4-complete-chatbot/
│
├── .env.example        # Template for environment variables
├── requirements.txt    # Package dependencies
├── app.py              # Complete Streamlit application
└── README.md           # This file
```

[← Back to Checkpoints](../README.md) | [← Back to Main README](../../README.md)