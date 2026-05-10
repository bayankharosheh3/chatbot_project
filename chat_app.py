import streamlit as st

st.title("Chatbot 💬")

st.info("Try typing: hello, help, or name")

if "messages" not in st.session_state:
    st.session_state.messages = []

responses = {
    "hello": "Hi there 👋",
    "help": "This chatbot responds using local Python logic.",
    "name": "I'm a simple Streamlit chatbot.",
    "python": "Python is used to build this application.",
    "streamlit": "Streamlit helps create web apps using Python.",
    "thank you":"you are welcome"
}

def generate_response(user_input):

    user_input = user_input.lower()

    for keyword, response in responses.items():

        if keyword in user_input:
            return response

    return f"I didn't understand that, try: hello, help, or name 🙂"

for message in st.session_state.messages:

    chat = st.chat_message(message["role"])
    chat.write(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    user_chat = st.chat_message("user")
    user_chat.write(prompt)

    response = generate_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    assistant_chat = st.chat_message("assistant")
    assistant_chat.write(response)