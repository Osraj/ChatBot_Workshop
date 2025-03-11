# 📊 Chatbot System Architecture

[← Back to Main README](../README.md)

This document provides an overview of the chatbot system architecture we'll be building in this workshop.

## System Overview

![Chatbot System Architecture](chatbot-architecture.png)

The chatbot we're building follows a modern web application architecture with AI integration:

1. **Frontend (User Interface)**
   - Built with Streamlit
   - Provides chat interface and customization controls
   - Displays conversation history

2. **Backend (Business Logic)**
   - Handles user input processing
   - Manages conversation state
   - Constructs API requests

3. **AI Service (Groq API)**
   - Processes natural language
   - Generates contextual responses
   - Supports different LLM models

## Data Flow

The diagram below illustrates the data flow in our chatbot application:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│             │     │             │     │             │     │             │
│    User     │────▶│  Streamlit  │────▶│  Python     │────▶│  Groq API   │
│  Interface  │     │  Web App    │     │  Backend    │     │  Service    │
│             │     │             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       ▲                                                           │
       │                                                           │
       │                                                           │
       └───────────────────────────────────────────────────────────┘
           Response displayed to user after AI generation
```

## Component Details

### 1. Streamlit Web App
- **Purpose**: Provides the user interface
- **Key Components**:
  - Chat message display
  - User input field
  - Customization sidebar
  - Session state management

### 2. Python Backend
- **Purpose**: Handles application logic
- **Key Components**:
  - Message history management
  - Environment variable handling
  - API client integration
  - Error handling

### 3. Groq API Service
- **Purpose**: Provides AI language capabilities
- **Key Components**:
  - Chat completion endpoint
  - Model selection (Llama, Mixtral, etc.)
  - Generation parameters
  - Response formatting

## Customization Layer

Our architecture includes a customization layer that allows users to:

- Select different AI models
- Adjust generation parameters
- Choose character personas
- Set response moods and styles

This is implemented through the Streamlit sidebar and passed as parameters to the Groq API.

## Detailed Component Interaction

1. **User sends a message**:
   - User types message in Streamlit chat input
   - Message is added to session state
   - UI updates to show the user message

2. **App processes the message**:
   - Combines message with conversation history
   - Adds system prompt based on customization
   - Constructs API request

3. **Groq API generates response**:
   - API receives request with messages and parameters
   - Selected model processes the input
   - AI generates appropriate response

4. **Response is displayed**:
   - App receives API response
   - Response is added to conversation history
   - UI updates to show AI message

## Implementation Benefits

This architecture provides several advantages:

- **Separation of concerns**: UI, logic, and AI are distinct components
- **Scalability**: Easy to modify individual components
- **Maintainability**: Clean structure for future enhancements
- **User control**: Extensive customization options

[← Back to Main README](../README.md)