# 🃏 Streamlit Quick Reference Card

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)

## App Basics

```bash
# Run app
streamlit run app.py

# Keyboard shortcuts in browser
r - Reload app
q - Stop app
```

## Core UI Elements

```python
# Page config
st.set_page_config(page_title="App Title", page_icon="🤖")

# Text elements
st.title("App Title")
st.header("Section Header")
st.markdown("**Bold** text")

# Layout
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
```

## Essential Widgets

```python
# Input widgets
text = st.text_input("Label")
num = st.number_input("Number", value=5)
option = st.selectbox("Choose", ["A", "B", "C"])
slider_val = st.slider("Value", 0, 100, 50)
checkbox = st.checkbox("Enable feature")

# Button
if st.button("Click me"):
    st.write("Button clicked!")
```

## Chat Components

```python
# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_input = st.chat_input("Say something")

# Add messages
with st.chat_message("user"):
    st.markdown(user_input)
```

## State Management

```python
# Initialize state
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Update state
st.session_state.counter += 1

# Reset app
st.rerun()
```

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)