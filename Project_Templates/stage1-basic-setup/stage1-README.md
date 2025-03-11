# Stage 1: Basic Setup

[← Back to Templates](../README.md) | [← Back to Main README](../../README.md)

This is the initial project setup with the basic structure needed to begin your chatbot project.

## Contents

- Basic project structure
- `.env` file template
- `requirements.txt` file with dependencies
- Placeholder `app.py` file

## Setup Instructions

1. Make sure you have Python installed (3.8 or higher recommended)

2. Install Miniconda if you haven't already (see main README)

3. Create and activate a conda environment:
   ```bash
   conda create -n chatbot-env python=3.10
   conda activate chatbot-env
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Rename `.env.example` to `.env` and add your API key:
   ```bash
   # On macOS/Linux
   cp .env.example .env
   
   # On Windows
   copy .env.example .env
   ```

6. Open `.env` in a text editor and replace `your_groq_api_key_here` with your actual Groq API key

## Next Steps

After completing these setup steps, you're ready to move on to building the Streamlit UI. You can either continue with this template and build the UI yourself or use the Stage 2 template that has the basic UI pre-built.

## File Structure

```
stage1-basic-setup/
│
├── .env.example        # Template for environment variables
├── requirements.txt    # Package dependencies
├── app.py              # Empty Streamlit application
└── README.md           # This file
```

[← Back to Templates](../README.md) | [← Back to Main README](../../README.md)