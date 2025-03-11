# Environment Setup Snippets

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)

Ready-to-use code snippets for setting up your development environment.

## Table of Contents
- [Environment Setup Snippets](#environment-setup-snippets)
  - [Table of Contents](#table-of-contents)
  - [Environment Variables](#environment-variables)
  - [Package Installation](#package-installation)
  - [Directory Structure](#directory-structure)
  - [Conda Environment](#conda-environment)
  - [Example App Initialization](#example-app-initialization)

## Environment Variables

```python
# .env file template
# Create a file named '.env' with this content
# and replace the values with your actual API keys

GROQ_API_KEY=your_groq_api_key_here
```

```python
# Loading environment variables in Python
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("GROQ_API_KEY")

# Check if API key is available
if not api_key:
    print("Warning: GROQ_API_KEY not found in environment variables")
else:
    print("API key loaded successfully")
```

## Package Installation

```bash
# Install required packages using pip
pip install streamlit groq python-dotenv

# Alternative: Install with version pinning
pip install streamlit==1.32.0 groq==0.4.0 python-dotenv==1.0.0

# Create requirements.txt
echo "streamlit>=1.32.0
groq>=0.4.0
python-dotenv>=1.0.0" > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

## Directory Structure

```python
# Script to create project directory structure
import os

def create_project_structure():
    # Create main project directory
    os.makedirs("groq-chatbot", exist_ok=True)
    os.chdir("groq-chatbot")
    
    # Create basic files
    with open("app.py", "w") as f:
        f.write("# Groq Chatbot App\n\nimport streamlit as st\n\nst.title('Groq Chatbot')\n")
    
    with open("requirements.txt", "w") as f:
        f.write("streamlit>=1.32.0\ngroq>=0.4.0\npython-dotenv>=1.0.0\n")
    
    with open(".env.example", "w") as f:
        f.write("GROQ_API_KEY=your_groq_api_key_here\n")
    
    with open("README.md", "w") as f:
        f.write("# Groq Chatbot\n\nA customizable chatbot using Groq API and Streamlit.\n")
    
    print("Project structure created successfully!")

# Run function to create structure
create_project_structure()
```

## Conda Environment

```bash
# Create and configure Conda environment

# Create new environment with Python 3.10
conda create -n chatbot-env python=3.10

# Activate the environment
conda activate chatbot-env

# Install pip packages
pip install streamlit groq python-dotenv

# List installed packages
conda list

# Export environment to file
conda env export > environment.yml

# Create environment from file
# conda env create -f environment.yml
```

```yaml
# Example environment.yml file
name: chatbot-env
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pip=23.0
  - pip:
    - streamlit>=1.32.0
    - groq>=0.4.0
    - python-dotenv>=1.0.0
```

## Example App Initialization

```python
# Basic app.py template
import streamlit as st
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("⚠️ Groq API Key not found. Please add it to your .env file.")
    st.stop()

try:
    client = groq.Client(api_key=api_key)
    st.success("✅ Connected to Groq API")
except Exception as e:
    st.error(f"⚠️ Error connecting to Groq API: {str(e)}")
    st.stop()

# Set page configuration
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Set app title
st.title("🤖 Custom Chatbot with Groq API")
st.write("Start chatting with the AI below!")

# Initialize chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Start building your chat interface here...
```

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)