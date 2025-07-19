import streamlit as st

# Basic response logic
def get_medical_response(user_input):
    user_input = user_input.lower()
    if "headache" in user_input:
        return "You might be experiencing a headache. Make sure to stay hydrated and rest. If it persists, consult a doctor."
    elif "fever" in user_input:
        return "You may have a fever. Monitor your temperature and consider seeing a doctor if it goes above 102°F."
    elif "cough" in user_input:
        return "A cough could be due to a cold or something more serious. If it's dry and persistent, consider a COVID-19 test."
    elif "stomach" in user_input or "abdominal" in user_input:
        return "Stomach pain can have many causes. Try to note the exact location and consult a physician if the pain is severe."
    elif "cold" in user_input:
        return "It might be a common cold. Drink plenty of fluids and get rest."
    else:
        return "Sorry, I couldn't understand. Please provide more details or consult a healthcare professional."

# Streamlit UI
st.set_page_config(page_title="🩺 Medical Chatbot", page_icon="💬")

st.title("🩺 Medical Chatbot")
st.write("I can help with basic medical symptom information. This is not a substitute for professional advice.")

# Chat session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    st.session_state.chat.append(("You", user_input))
    response = get_medical_response(user_input)
    st.session_state.chat.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
