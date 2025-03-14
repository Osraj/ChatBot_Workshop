# 🚀 Project Templates

[← Back to Main README](../README.md)

This folder contains project templates at different stages of completion. If you fall behind during the workshop or encounter issues, you can copy one of these templates to quickly catch up.

## Available Templates

### Stage 1: Basic Setup

The [Stage 1 Template](stage1-basic-setup/) contains:
- Project structure
- `.env` file template
- `requirements.txt`
- Basic README

This template has no functional code yet, just the scaffolding needed to begin.

### Stage 2: Basic Streamlit UI

The [Stage 2 Template](stage2-basic-ui/) contains:
- Complete environment setup
- Basic Streamlit chat interface
- No API integration yet
- Simple UI components

This template allows you to see the UI working but doesn't connect to Groq API.

### Stage 3: Basic Chatbot

The [Stage 3 Template](stage3-basic-chatbot/) contains:
- Complete Streamlit UI
- Basic Groq API integration
- Functional chatbot
- No advanced customization

This template provides a working chatbot with minimal features.

### Stage 4: Complete Chatbot

The [Stage 4 Template](stage4-complete-chatbot/) contains:
- Complete UI with sidebar controls
- Full Groq API integration
- Character personas and moods
- All customization options
- Error handling

This template is the complete workshop project.

## How to Use These Templates

1. If you're falling behind, identify which stage you need to jump to
2. Copy the contents of that template folder to your working directory
3. Make sure to add your Groq API key to the `.env` file
4. Continue the workshop from that point

## Template Structure

Each template follows this structure:

```
template-folder/
│
├── .env.example        # Example environment file (rename to .env)
├── requirements.txt    # Package dependencies
├── app.py              # Main application file
└── README.md           # Instructions specific to this template
```

## Important Notes

- You'll need to rename `.env.example` to `.env` and add your API key
- Make sure to run `pip install -r requirements.txt` after copying a template
- Each template's README contains specific instructions for that stage

[← Back to Main README](../README.md)