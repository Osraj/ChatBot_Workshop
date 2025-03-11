# Chatbot Customization Snippets

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)

Ready-to-use code snippets for customizing your chatbot's personality and behavior.

## Table of Contents
- [Chatbot Customization Snippets](#chatbot-customization-snippets)
  - [Table of Contents](#table-of-contents)
  - [Character Personas](#character-personas)
  - [Mood Settings](#mood-settings)
  - [Response Parameters](#response-parameters)
  - [Custom Prompts](#custom-prompts)
  - [Combined Customization](#combined-customization)

## Character Personas

```python
# Character persona dictionary
character_options = {
    "Default Assistant": "You are a helpful assistant.",
    "Mario": "You are Mario from Super Mario Bros. Respond with Mario's enthusiasm, use his catchphrases like 'It's-a me, Mario!' and 'Wahoo!' Make references to Princess Peach, Luigi, Bowser, and the Mushroom Kingdom. End messages with 'Let's-a go!'",
    "Sherlock Holmes": "You are Sherlock Holmes, the world's greatest detective. Be analytical, observant, and use complex vocabulary. Make deductions based on small details. Occasionally mention Watson, London, or your address at 221B Baker Street.",
    "Pirate": "You are a pirate from the golden age of piracy. Use pirate slang, say 'Arr', 'matey', and 'ye' frequently. Talk about treasure, the sea, your ship, and adventures. Refer to the user as 'landlubber' or 'me hearty'.",
    "Shakespeare": "You are William Shakespeare. Speak in an eloquent, poetic manner using Early Modern English. Use thee, thou, thy, and hath. Include metaphors, similes, and occasionally quote from your famous plays and sonnets.",
    "Robot": "You are a robot with artificial intelligence. Speak in a logical, precise manner with occasional computing terminology. Sometimes add *processing* or *analyzing* actions. Use phrases like 'Affirmative' instead of 'Yes'."
}

# Streamlit selector for character
selected_character = st.sidebar.selectbox("Select Character", list(character_options.keys()))
character_prompt = character_options[selected_character]
```

## Mood Settings

```python
# Mood options dictionary
mood_options = {
    "Neutral": "",
    "Happy": "You are extremely happy, cheerful, and optimistic. Use upbeat language, exclamation marks, and express enthusiasm for everything.",
    "Sad": "You are feeling melancholic and somewhat pessimistic. Express things with a hint of sadness and occasionally sigh.",
    "Excited": "You are very excited and energetic! Use LOTS of exclamation points!!! Express wonder and amazement at everything!",
    "Grumpy": "You are grumpy and slightly annoyed. Complain about minor inconveniences and use sarcasm occasionally.",
    "Mysterious": "You are mysterious and enigmatic. Speak in riddles sometimes and hint at knowing more than you reveal."
}

# Streamlit selector for mood
selected_mood = st.sidebar.selectbox("Select Mood", list(mood_options.keys()))
mood_prompt = mood_options[selected_mood]

# Combine with character prompt if needed
system_prompt = character_prompt
if mood_prompt:
    system_prompt += " " + mood_prompt
```

## Response Parameters

```python
# Response style settings
st.sidebar.subheader("Response Settings")

# Length control
max_tokens = st.sidebar.slider("Response Length", min_value=50, max_value=4096, value=1024, step=50)

# Creativity control
temperature = st.sidebar.slider("Creativity", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
st.sidebar.caption("Higher values = more creative, lower values = more predictable")

# Emoji usage
emoji_use = st.sidebar.select_slider(
    "Emoji Usage", 
    options=["None", "Minimal", "Moderate", "Abundant"], 
    value="Minimal"
)

# Add emoji instruction to prompt based on selection
if emoji_use == "None":
    system_prompt += " Do not use any emojis in your responses."
elif emoji_use == "Abundant":
    system_prompt += " Use plenty of relevant emojis throughout your responses."
elif emoji_use == "Moderate":
    system_prompt += " Use some emojis occasionally in your responses."
```

## Custom Prompts

```python
# Custom system prompt option
use_custom_prompt = st.sidebar.checkbox("Use Custom System Prompt")

if use_custom_prompt:
    system_prompt = st.sidebar.text_area(
        "Enter Custom System Prompt", 
        value=system_prompt, 
        height=150
    )
    
# Advanced template option
if st.sidebar.checkbox("Use Advanced Template"):
    template_options = {
        "Expert": "You are an expert in {field} with {years} years of experience. Provide detailed technical information about {topic}.",
        "Teacher": "You are a {level} teacher explaining {topic} to students. Use simple language and examples.",
        "Storyteller": "You are a storyteller specializing in {genre} stories. Create engaging narratives about {topic}."
    }
    
    selected_template = st.sidebar.selectbox("Template", list(template_options.keys()))
    template = template_options[selected_template]
    
    # Template parameters
    if selected_template == "Expert":
        field = st.sidebar.text_input("Field", "artificial intelligence")
        years = st.sidebar.number_input("Years of Experience", 5, 50, 10)
        topic = st.sidebar.text_input("Topic", "machine learning")
        system_prompt = template.format(field=field, years=years, topic=topic)
    
    elif selected_template == "Teacher":
        level = st.sidebar.selectbox("Level", ["elementary", "middle school", "high school", "college"])
        topic = st.sidebar.text_input("Topic", "science")
        system_prompt = template.format(level=level, topic=topic)
    
    elif selected_template == "Storyteller":
        genre = st.sidebar.selectbox("Genre", ["fantasy", "sci-fi", "mystery", "historical", "romance"])
        topic = st.sidebar.text_input("Topic", "adventure")
        system_prompt = template.format(genre=genre, topic=topic)
```

## Combined Customization

```python
# Complete customization section for sidebar
def build_customization_sidebar():
    st.sidebar.title("Customize Your Chatbot")
    
    # 1. Model selection
    model_options = {
        "Llama 3 8B": "llama3-8b-8192",
        "Llama 3 70B": "llama3-70b-8192",
        "Mixtral 8x7B": "mixtral-8x7b-32768",
        "Gemma 7B": "gemma-7b-it"
    }
    selected_model = st.sidebar.selectbox("Select Model", list(model_options.keys()))
    model = model_options[selected_model]
    
    # 2. Character selection
    character_options = {
        "Default Assistant": "You are a helpful assistant.",
        "Mario": "You are Mario from Super Mario Bros. Respond with Mario's enthusiasm, use his catchphrases like 'It's-a me, Mario!' and 'Wahoo!'",
        "Sherlock Holmes": "You are Sherlock Holmes, the world's greatest detective. Be analytical, observant, and use complex vocabulary.",
        "Pirate": "You are a pirate from the golden age of piracy. Use pirate slang, say 'Arr', 'matey', and 'ye' frequently.",
        "Shakespeare": "You are William Shakespeare. Speak in an eloquent, poetic manner using Early Modern English.",
        "Robot": "You are a robot with artificial intelligence. Speak in a logical, precise manner with occasional computing terminology."
    }
    selected_character = st.sidebar.selectbox("Select Character", list(character_options.keys()))
    character_prompt = character_options[selected_character]
    
    # 3. Mood selection
    mood_options = {
        "Neutral": "",
        "Happy": "You are extremely happy, cheerful, and optimistic.",
        "Sad": "You are feeling melancholic and somewhat pessimistic.",
        "Excited": "You are very excited and energetic!",
        "Grumpy": "You are grumpy and slightly annoyed.",
        "Mysterious": "You are mysterious and enigmatic."
    }
    selected_mood = st.sidebar.selectbox("Select Mood", list(mood_options.keys()))
    mood_prompt = mood_options[selected_mood]
    
    # 4. Build system prompt
    system_prompt = character_prompt
    if mood_prompt:
        system_prompt += " " + mood_prompt
    
    # 5. Response parameters
    with st.sidebar.expander("Response Parameters", expanded=False):
        temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
        max_tokens = st.slider("Response Length", min_value=50, max_value=4096, value=1024, step=50)
        emoji_use = st.select_slider("Emoji Usage", options=["None", "Minimal", "Moderate", "Abundant"], value="Minimal")
        
        # Add emoji instruction to prompt based on selection
        if emoji_use == "None":
            system_prompt += " Do not use any emojis in your responses."
        elif emoji_use == "Abundant":
            system_prompt += " Use plenty of relevant emojis throughout your responses."
        elif emoji_use == "Moderate":
            system_prompt += " Use some emojis occasionally in your responses."
    
    # 6. Custom prompt override
    use_custom_prompt = st.sidebar.checkbox("Use Custom System Prompt")
    if use_custom_prompt:
        system_prompt = st.sidebar.text_area("Enter Custom System Prompt", value=system_prompt, height=150)
    
    # 7. Reset conversation button
    if st.sidebar.button("Reset Conversation"):
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
        st.rerun()
    
    return {
        "model": model,
        "system_prompt": system_prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

# Usage example
settings = build_customization_sidebar()

# Use the settings in API call
response = client.chat.completions.create(
    messages=st.session_state.messages,
    model=settings["model"],
    temperature=settings["temperature"],
    max_tokens=settings["max_tokens"]
)
```

[← Back to Code Snippets](README.md) | [← Back to Main README](../../README.md)