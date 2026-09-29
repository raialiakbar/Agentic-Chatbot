from agentic_chatbot_backend import chatbot 
from langchain_core.messages import BaseMessage, HumanMessage
import streamlit as st


 
thread_id = 1
config = {"configurable": {"thread_id": thread_id}}

st.title("Agentic Chatbot with Langgraph")



user_input = st.chat_input('Type here')

if user_input:
    with st.chat_message('user'):
        st.text(user_input)
    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]},config=config)
    ai_message = response["messages"][-1].content[0]["text"]
    with st.chat_message('assistant'):
        st.write(ai_message)







