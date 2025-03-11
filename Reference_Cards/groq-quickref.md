# 🃏 Groq API Quick Reference Card

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)

## Setup & Authentication

```python
# Import libraries
import groq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))
```

## Simple Chat Completion

```python
# Basic chat completion
response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    model="llama3-8b-8192"
)

# Get response text
assistant_response = response.choices[0].message.content
print(assistant_response)
```

## Models Reference

| Model | API ID | Best For |
|-------|--------|----------|
| Llama 3 8B | llama3-8b-8192 | Fast responses |
| Llama 3 70B | llama3-70b-8192 | Complex tasks |
| Mixtral 8x7B | mixtral-8x7b-32768 | Long context |
| Gemma 7B | gemma-7b-it | Balanced |

## Key Parameters

```python
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=messages,
    temperature=0.7,          # 0.0-1.0 (creativity)
    max_tokens=1024,          # Response length
    frequency_penalty=0.0,    # -2.0 to 2.0
    presence_penalty=0.0      # -2.0 to 2.0
)
```

## Error Handling

```python
try:
    response = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"
    )
except Exception as e:
    print(f"Error: {str(e)}")
```

## Workshop Models

```python
model_options = {
    "Llama 3 8B": "llama3-8b-8192",
    "Llama 3 70B": "llama3-70b-8192",
    "Mixtral 8x7B": "mixtral-8x7b-32768",
    "Gemma 7B": "gemma-7b-it"
}
```

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)