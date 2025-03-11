# 📋 Streamlit Commands Cheat Sheet

[← Back to Main README](README.md) | [View All Cheat Sheets](cheatsheets.md)

This cheat sheet provides a quick reference for Streamlit commands and components when building interactive web applications.

## Table of Contents
- [📋 Streamlit Commands Cheat Sheet](#-streamlit-commands-cheat-sheet)
  - [Table of Contents](#table-of-contents)
  - [Basic Commands](#basic-commands)
  - [Configuration](#configuration)
  - [Page Layout Components](#page-layout-components)
  - [Sidebar](#sidebar)
  - [Display Elements](#display-elements)
  - [Input Widgets](#input-widgets)
  - [Chat Interface Components](#chat-interface-components)
  - [State Management](#state-management)
  - [Performance Optimization](#performance-optimization)
  - [Status and Progress](#status-and-progress)
  - [Common Issues and Solutions](#common-issues-and-solutions)
  - [Tips for Workshop](#tips-for-workshop)

## Basic Commands

```bash
# Run a Streamlit app
streamlit run app.py

# Run on specific port
streamlit run app.py --server.port 8501

# Run with server address
streamlit run app.py --server.address 0.0.0.0

# Clear cache
streamlit cache clear

# Show Streamlit version
streamlit --version
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Configuration

```bash
# View all config options
streamlit config show

# Set a config option
streamlit config set server.maxUploadSize 50

# Create default config file
streamlit config show > .streamlit/config.toml
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Page Layout Components

```python
# Set page configuration
st.set_page_config(
    page_title="App Title",
    page_icon="🤖",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"  # or "collapsed"
)

# Add a title
st.title("Application Title")

# Add a header
st.header("Section Header")

# Add a subheader
st.subheader("Subsection")

# Add text
st.text("Plain text")

# Add markdown
st.markdown("**Bold** and _italic_ text")

# Add a divider
st.divider()

# Create columns
col1, col2 = st.columns(2)  # Two equal columns
with col1:
    st.write("Content for column 1")
with col2:
    st.write("Content for column 2")

# Create columns with different widths
col1, col2, col3 = st.columns([1, 2, 1])  # Ratio 1:2:1

# Create tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content for tab 1")
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Sidebar

```python
# Add components to sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.header("Sidebar Header")

# Sidebar with expander
with st.sidebar.expander("Advanced Options", expanded=False):
    st.write("Expanded content here")

# Sidebar divider
st.sidebar.divider()
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Display Elements

```python
# Display text
st.write("Dynamic content")

# Display code
st.code("def hello_world():\n    print('Hello, World!')", language="python")

# Display LaTeX
st.latex(r"e^{i\pi} + 1 = 0")

# Display data
st.dataframe(my_dataframe)  # Interactive dataframe
st.table(my_table_data)     # Static table
st.json(my_json_data)       # JSON viewer

# Display media
st.image("image.jpg", caption="Image caption", width=300)
st.audio("audio.mp3")
st.video("video.mp4")
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Input Widgets

```python
# Text input
user_input = st.text_input("Enter text:", "Default value")

# Text area (multi-line)
long_text = st.text_area("Enter long text:", "Default text", height=150)

# Number input
num = st.number_input("Enter a number:", min_value=0, max_value=100, value=50, step=5)

# Slider
val = st.slider("Select a value:", 0, 100, 50)
range_vals = st.slider("Select a range:", 0, 100, (25, 75))

# Select box (dropdown)
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])

# Multi-select
options = st.multiselect("Select multiple:", ["A", "B", "C", "D"])

# Checkbox
checked = st.checkbox("Check me", value=False)

# Radio buttons
choice = st.radio("Choose one:", ["Option 1", "Option 2"])

# Button
if st.button("Click me"):
    st.write("Button clicked!")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])

# Color picker
color = st.color_picker("Pick a color:", "#00f900")

# Date input
date = st.date_input("Select a date:")

# Time input
time = st.time_input("Select a time:")
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Chat Interface Components

```python
# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Say something")

# Add a message to chat
with st.chat_message("user"):
    st.markdown(user_input)

# Show assistant message with placeholder for streaming
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    message_placeholder.markdown("Thinking...")
    # Later update with:
    message_placeholder.markdown("Final response")
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## State Management

```python
# Initialize session state variables
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Update session state
st.session_state.counter += 1

# Access session state
st.write(f"Counter: {st.session_state.counter}")

# Button to update state
if st.button("Increment"):
    st.session_state.counter += 1

# Button to reset state
if st.button("Reset"):
    st.session_state.counter = 0
    st.rerun()  # Rerun the app with new state

# Session state callback
def callback_function():
    st.session_state.value = "New value"

st.button("Run Callback", on_click=callback_function)
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Performance Optimization

```python
# Cache data (memoize)
@st.cache_data
def get_data():
    # Expensive operation
    return expensive_computation()

data = get_data()  # Only runs once, then uses cached result

# Cache with TTL (time to live)
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_external_data():
    return fetch_from_api()

# Clear specific cache entry
get_data.clear()

# Cache resource (connections etc.)
@st.cache_resource
def get_database_connection():
    return create_db_connection()
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Status and Progress

```python
# Display info message
st.info("This is an information message")

# Display success message
st.success("Operation successful!")

# Display warning message
st.warning("Warning: this action is risky")

# Display error message
st.error("Error: something went wrong")

# Display spinner
with st.spinner("Processing..."):
    time.sleep(2)  # Simulate long operation
    st.success("Done!")

# Display progress bar
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)

# Balloons and snow
st.balloons()  # Show balloons animation
st.snow()      # Show snow animation
```

[Back to Top](#-streamlit-commands-cheat-sheet)

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| App not updating | Check if you're using `st.cache` correctly |
| Widget state lost | Use `st.session_state` to persist values |
| Port already in use | Kill the process or use a different port (--server.port) |
| "No module named streamlit" | Install with `pip install streamlit` |
| Slow performance | Cache expensive operations with `@st.cache_data` |
| App rerunning constantly | Avoid changing session state outside of callbacks |

[Back to Top](#-streamlit-commands-cheat-sheet)

## Tips for Workshop

- Start with simpler components and add complexity gradually
- Use `st.session_state` to persist chat history between interactions
- Organize complex apps into separate Python files and import functions
- For production, configure Streamlit to run as a service

[Back to Top](#-streamlit-commands-cheat-sheet)

[← Back to Main README](README.md) | [View All Cheat Sheets](cheatsheets.md)