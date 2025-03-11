# Stage 2: Basic Streamlit UI

[← Back to Templates](../README.md) | [← Back to Main README](../../README.md)

This template includes a basic Streamlit UI for your chatbot, with a chat interface but no API integration yet.

## Contents

- Complete environment setup
- Basic Streamlit chat interface
- No API integration yet
- Simple UI components

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

## What This Template Includes

- A complete Streamlit UI with:
  - Chat interface
  - Message history
  - User input field
  - Placeholder for chat responses (no actual API calls yet)

## Next Steps

After testing the UI, you can integrate the Groq API to make your chatbot respond to user inputs. You can either modify this template yourself or use the Stage 3 template that has the basic API integration pre-built.

## File Structure

```
stage2-basic-ui/
│
├── .env.example        # Template for environment variables
├── requirements.txt    # Package dependencies
├── app.py              # Streamlit application with UI
└── README.md           # This file
```

[← Back to Templates](../README.md) | [← Back to Main README](../../README.md)