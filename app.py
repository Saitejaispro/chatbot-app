import streamlit as st
import re

# Initialize session state
if 'name' not in st.session_state:
    st.session_state.name = None
if 'age' not in st.session_state:
    st.session_state.age = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Extract age from text
def extract_age(text):
    match = re.search(r"\b(\d{1,2})\b", text)
    if match:
        age = int(match.group(1))
        if 5 < age < 100:
            return age
    return None

# Generate bot reply
def get_reply(msg):
    if not st.session_state.name:
        st.session_state.name = msg.strip()
        return f"Hi {st.session_state.name}, nice to meet you! May I know your age?"

    if not st.session_state.age:
        age = extract_age(msg)
        if age:
            st.session_state.age = age
            return f"Thanks, {st.session_state.name}! You're {age} years old. How can I help you today?"
        return "Please enter a valid age."

    # Simple customer service replies
    msg = msg.lower()
    if "refund" in msg:
        return "I understand you want a refund. Please provide your order ID."
    elif "late" in msg:
        return "Sorry for the delay. I’ll escalate this issue right away."
    elif "problem" in msg or "help" in msg:
        return "I'm here to help. Please explain your issue."
    elif "bye" in msg or "thank" in msg:
        return "Thank you for chatting! Have a great day!"
    else:
        return "Thanks for sharing. We’ve noted your concern."

# Page title
st.set_page_config(page_title="Customer Service Chatbot")
st.title("🤖 Customer Service Chatbot")
st.write("Hi there! I'm here to help. Start by entering your name below.")

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")

# User input
user_input = st.text_input("Your message", key="input")

if user_input:
    bot_reply = get_reply(user_input)
    st.session_state.chat_history.append({
        "user": user_input,
        "bot": bot_reply
    })
    st.experimental_rerun()
