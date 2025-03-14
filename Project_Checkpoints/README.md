# 🚀 Project Checkpoints

[← Back to Main README](../README.md)

This folder contains project Checkpoints at different stages of completion. If you fall behind during the workshop or encounter issues, you can copy one of these Checkpoints to quickly catch up.

## Available Checkpoints

### Stage 1: Basic Setup

The [Stage 1 Checkpoint](stage1-basic-setup/) contains:
- Project structure
- `.env` file template
- `requirements.txt`
- Basic README

This Checkpoint has no functional code yet, just the scaffolding needed to begin.

### Stage 2: Basic Streamlit UI

The [Stage 2 Checkpoint](stage2-basic-ui/) contains:
- Complete environment setup
- Basic Streamlit chat interface
- No API integration yet
- Simple UI components

This Checkpoint allows you to see the UI working but doesn't connect to Groq API.

### Stage 3: Basic Chatbot

The [Stage 3 Checkpoint](stage3-basic-chatbot/) contains:
- Complete Streamlit UI
- Basic Groq API integration
- Functional chatbot
- No advanced customization

This Checkpoint provides a working chatbot with minimal features.

### Stage 4: Complete Chatbot

The [Stage 4 Checkpoint](stage4-complete-chatbot/) contains:
- Complete UI with sidebar controls
- Full Groq API integration
- Character personas and moods
- All customization options
- Error handling

This Checkpoint is the complete workshop project.

## How to Use These Checkpoints

1. If you're falling behind, identify which stage you need to jump to
2. Copy the contents of that Checkpoint folder to your working directory
3. Make sure to add your Groq API key to the `.env` file
4. Continue the workshop from that point

## Checkpoint Structure

Each Checkpoint follows this structure:

```
Checkpoint-folder/
│
├── .env.example        # Example environment file (rename to .env)
├── requirements.txt    # Package dependencies
├── app.py              # Main application file
└── README.md           # Instructions specific to this Checkpoint
```

## Important Notes

- You'll need to rename `.env.example` to `.env` and add your API key
- Make sure to run `pip install -r requirements.txt` after copying a Checkpoint
- Each Checkpoint's README contains specific instructions for that stage

[← Back to Main README](../README.md)