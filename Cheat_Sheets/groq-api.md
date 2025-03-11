# 📋 Groq API Cheat Sheet

[← Back to Main README](README.md) | [View All Cheat Sheets](cheatsheets.md)

This cheat sheet provides a quick reference for using the Groq API to create AI-powered applications.

## Table of Contents
- [📋 Groq API Cheat Sheet](#-groq-api-cheat-sheet)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Authentication](#authentication)
  - [Basic API Usage](#basic-api-usage)
    - [Simple Chat Completion](#simple-chat-completion)
    - [Multi-turn Conversation](#multi-turn-conversation)
  - [Advanced Parameters](#advanced-parameters)
    - [Complete Parameters Example](#complete-parameters-example)
    - [Generation Parameters Explained](#generation-parameters-explained)
  - [Available Models](#available-models)
    - [Model Comparison](#model-comparison)
    - [Model Selection Guidelines](#model-selection-guidelines)
  - [Advanced Techniques](#advanced-techniques)
    - [System Prompts](#system-prompts)
    - [Error Handling](#error-handling)
    - [Retry Strategy](#retry-strategy)
  - [Integration with Streamlit](#integration-with-streamlit)
    - [Chat Interface with Groq](#chat-interface-with-groq)
  - [Common Error Messages](#common-error-messages)
  - [Tips for Workshop](#tips-for-workshop)

## Getting Started

### Installation

```bash
# Install Groq client library
pip install groq

# Install additional helper packages
pip install python-dotenv  # For environment variables
```

### Authentication

```python
# Import the module
import groq
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize client with API key
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

# Alternatively, set API key directly
client = groq.Client(api_key="your-api-key-here")
```

[Back to Top](#-groq-api-cheat-sheet)

## Basic API Usage

### Simple Chat Completion

```python
# Generate a simple completion
response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about AI."}
    ],
    model="llama3-8b-8192"
)

# Access the response
assistant_message = response.choices[0].message.content
print(assistant_message)
```

### Multi-turn Conversation

```python
# Store conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Add user message
user_input = "What is machine learning?"
messages.append({"role": "user", "content": user_input})

# Get response
response = client.chat.completions.create(
    messages=messages,
    model="llama3-8b-8192"
)

# Add assistant response to history
assistant_response = response.choices[0].message.content
messages.append({"role": "assistant", "content": assistant_response})

# Continue conversation
user_input = "Give me some examples of applications."
messages.append({"role": "user", "content": user_input})

# Get next response
response = client.chat.completions.create(
    messages=messages,
    model="llama3-8b-8192"
)
```

[Back to Top](#-groq-api-cheat-sheet)

## Advanced Parameters

### Complete Parameters Example

```python
response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "system", "content": "You are a creative writing assistant."},
        {"role": "user", "content": "Write a short story about space exploration."}
    ],
    temperature=0.8,           # Controls randomness (0-1)
    max_tokens=2000,           # Maximum response length
    top_p=0.95,                # Nucleus sampling parameter
    frequency_penalty=0.5,     # Discourages repetition of tokens
    presence_penalty=0.5       # Encourages topic diversity
)
```

### Generation Parameters Explained

| Parameter | Description | Range | Default | When to Adjust |
|-----------|-------------|-------|---------|----------------|
| temperature | Controls randomness | 0.0-1.0 | 0.7 | ↑ for creativity, ↓ for determinism |
| max_tokens | Limits response length | 1-4096 | 1024 | ↑ for longer outputs, ↓ for conciseness |
| top_p | Nucleus sampling | 0.0-1.0 | 1.0 | Lower to limit token selection |
| frequency_penalty | Discourages repetition | -2.0-2.0 | 0.0 | ↑ to reduce repetition |
| presence_penalty | Topic diversity | -2.0-2.0 | 0.0 | ↑ to encourage new topics |

[Back to Top](#-groq-api-cheat-sheet)

## Available Models

### Model Comparison

| Model | API Identifier | Tokens | Strengths | Ideal Use Cases |
|-------|----------------|--------|-----------|----------------|
| Llama 3 8B | `llama3-8b-8192` | 8,192 | Fast, efficient | Simple chatbots, Q&A, testing |
| Llama 3 70B | `llama3-70b-8192` | 8,192 | Strong reasoning | Complex tasks, content creation |
| Mixtral 8x7B | `mixtral-8x7b-32768` | 32,768 | Long context | Document analysis, summarization |
| Gemma 7B | `gemma-7b-it` | 8,192 | Instruction tuned | General purpose assistant |

### Model Selection Guidelines

- **Llama 3 8B**: Best for quick responses, basic Q&A, and prototyping
- **Llama 3 70B**: Best for complex reasoning, creative writing, and detailed responses
- **Mixtral 8x7B**: Best for long documents and conversations that require extensive context
- **Gemma 7B**: Best for balanced performance when following instructions

[Back to Top](#-groq-api-cheat-sheet)

## Advanced Techniques

### System Prompts

Effective system prompts help control the assistant's behavior:

```python
# Expert assistant
system_prompt = """You are an expert AI assistant with deep knowledge 
across many fields. Provide detailed, accurate, and scholarly responses 
with citations where appropriate."""

# Creative assistant
system_prompt = """You are a creative writing assistant. Generate imaginative,
engaging content that captures the reader's attention. Feel free to use vivid
descriptions and narrative techniques."""

# Technical assistant
system_prompt = """You are a programming assistant specializing in Python.
Provide clean, well-commented code examples with explanations.
Focus on best practices and efficient solutions."""
```

### Error Handling

```python
try:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello"}],
        model="llama3-8b-8192"
    )
    print(response.choices[0].message.content)
except Exception as e:
    error_type = type(e).__name__
    error_message = str(e)
    print(f"Error ({error_type}): {error_message}")
    
    # Handle specific errors
    if "rate limit" in error_message.lower():
        print("Rate limit exceeded. Waiting before retry...")
        time.sleep(5)  # Wait and retry
    elif "authentication" in error_message.lower():
        print("Check your API key")
```

### Retry Strategy

```python
import time
import random

def call_groq_with_retry(messages, model, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = client.chat.completions.create(
                messages=messages,
                model=model
            )
            return response
        except Exception as e:
            retries += 1
            if retries >= max_retries:
                raise e
            
            # Exponential backoff with jitter
            wait_time = (2 ** retries) + random.uniform(0, 1)
            print(f"Retry {retries}/{max_retries} after {wait_time:.2f}s")
            time.sleep(wait_time)
```

[Back to Top](#-groq-api-cheat-sheet)

## Integration with Streamlit

### Chat Interface with Groq

```python
import streamlit as st
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat messages (excluding system message)
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
                model="llama3-8b-8192"
            )
            
            assistant_response = response.choices[0].message.content
            
            # Display the response
            message_placeholder.markdown(assistant_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        except Exception as e:
            message_placeholder.error(f"Error: {str(e)}")
```

[Back to Top](#-groq-api-cheat-sheet)

## Common Error Messages

| Error | Possible Causes | Solution |
|-------|-----------------|----------|
| API key error | Invalid key, not set in .env | Check .env file and credentials |
| Rate limit exceeded | Too many requests | Implement exponential backoff retry |
| Context length exceeded | Input too long for model | Reduce context or use a model with longer context |
| Bad gateway | Temporary service issue | Retry after a short delay |
| Timeout | Response taking too long | Reduce max_tokens or use smaller model |

[Back to Top](#-groq-api-cheat-sheet)

## Tips for Workshop

- Start with the simplest model (Llama 3 8B) for testing
- Use descriptive system prompts to set behavior expectations
- Implement proper error handling for production applications
- Consider response streaming for better user experience
- Keep API keys secure using environment variables

[Back to Top](#-groq-api-cheat-sheet)

[← Back to Main README](README.md) | [View All Cheat Sheets](cheatsheets.md)