from agentic_chatbot_backend import chatbot 
from langchain_core.messages import BaseMessage, HumanMessage
import streamlit as st


st.title("Agentic Chatbot with Langgraph")

 
thread_id = 1
config = {"configurable": {"thread_id": thread_id}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
                                





user_input = st.chat_input('Type here')

if user_input:
    # first add the message to message history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]},config=config)
    ai_message = response["messages"][-1].content[0]["text"]
    # then add the response to history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.write(ai_message)







