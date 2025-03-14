# Stage 3: Basic Chatbot

[← Back to Checkpoints](../README.md) | [← Back to Main README](../../README.md)

This Checkpoint includes a functional chatbot with basic Groq API integration, but without advanced customization options.

## Contents

- Complete Streamlit UI
- Basic Groq API integration
- Functional chatbot
- No advanced customization

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
  - Basic API calls
  - Error handling
  - Default settings
- Basic session state management

## Next Steps

Now that you have a working chatbot, you can add advanced customization options like model selection, temperature control, character personas, etc. You can either modify this Checkpoint yourself or use the Stage 4 Checkpoint that has all the customization options pre-built.

## File Structure

```
stage3-basic-chatbot/
│
├── .env.example        # Template for environment variables
├── requirements.txt    # Package dependencies
├── app.py              # Streamlit application with API integration
└── README.md           # This file
```

[← Back to Checkpoints](../README.md) | [← Back to Main README](../../README.md)