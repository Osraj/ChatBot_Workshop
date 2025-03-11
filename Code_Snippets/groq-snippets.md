# Groq API Code Snippets

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)

Ready-to-use Groq API code snippets for your chatbot project.

## Table of Contents
- [Groq API Code Snippets](#groq-api-code-snippets)
  - [Table of Contents](#table-of-contents)
  - [Client Initialization](#client-initialization)
  - [Basic Chat Completion](#basic-chat-completion)
  - [Conversation Management](#conversation-management)
  - [Error Handling](#error-handling)
  - [Advanced Parameters](#advanced-parameters)

## Client Initialization

```python
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
try:
    client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))
    # Test connection
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello"}],
        model="llama3-8b-8192",
        max_tokens=10
    )
    print("API client successfully initialized")
except Exception as e:
    print(f"Error initializing API client: {str(e)}")
```

## Basic Chat Completion

```python
# Simple completion example
def get_ai_response(user_input, model="llama3-8b-8192"):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        model=model
    )
    return response.choices[0].message.content

# Call the function
user_question = "What is machine learning?"
ai_answer = get_ai_response(user_question)
print(ai_answer)
```

## Conversation Management

```python
# Initialize conversation with system prompt
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Function to add user message and get response
def chat_turn(user_input, model="llama3-8b-8192", temperature=0.7):
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    
    # Get response from API
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature
    )
    
    # Extract assistant message
    assistant_message = response.choices[0].message.content
    
    # Add assistant message to history
    messages.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message

# Example conversation
response1 = chat_turn("What is Python?")
print("Response 1:", response1)

response2 = chat_turn("How is it different from JavaScript?")
print("Response 2:", response2)
```

## Error Handling

```python
def safe_api_call(messages, model, max_retries=3):
    retries = 0
    backoff_time = 1  # Start with 1 second
    
    while retries < max_retries:
        try:
            response = client.chat.completions.create(
                messages=messages,
                model=model
            )
            return response.choices[0].message.content
        
        except Exception as e:
            error_type = type(e).__name__
            error_message = str(e)
            
            # Handle specific error types
            if "rate limit" in error_message.lower():
                print(f"Rate limit exceeded. Retrying in {backoff_time} seconds...")
                time.sleep(backoff_time)
                backoff_time *= 2  # Exponential backoff
            
            elif "authentication" in error_message.lower():
                print("Authentication error. Check your API key.")
                return "Error: API key is invalid or missing."
            
            elif "not found" in error_message.lower():
                print(f"Model '{model}' not found. Try a different model.")
                return f"Error: Model '{model}' not available."
            
            else:
                print(f"Unexpected error: {error_type} - {error_message}")
                
            retries += 1
            
            if retries >= max_retries:
                return f"Error after {max_retries} attempts: {error_message}"
```

## Advanced Parameters

```python
# Advanced parameters example
def generate_creative_content(prompt, creativity=0.8, length=2000):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system", 
                "content": "You are a creative writing assistant known for vivid descriptions."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        model="llama3-70b-8192",      # Using larger model for creative tasks
        temperature=creativity,        # Higher temperature for more creativity
        max_tokens=length,             # Control response length
        top_p=0.95,                    # Nucleus sampling (slightly narrowed)
        frequency_penalty=0.5,         # Reduce repetition of phrases
        presence_penalty=0.5           # Encourage topic diversity
    )
    
    return response.choices[0].message.content

# Example usage
story_prompt = "Write a short story about a robot discovering emotions."
story = generate_creative_content(story_prompt)
print(story)
```

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)