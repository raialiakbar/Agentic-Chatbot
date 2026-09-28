from agentic_chatbot_backend import chatbot 
from langchain_core.messages import BaseMessage, HumanMessage

config = {"configurable": {"thread_id": "1"}}

response = chatbot.invoke(
    {"messages": [HumanMessage(content="What is the capital of Germany?")]},
    config=config
)

print(response["messages"][-1].content)