## There are 3 types of messages: SystemMessage, HumanMessage, and AIMessage.
## SystemMessage is used to set the context for the conversation.
## HumanMessage is used for user input, and AIMessage is used for the AI's response.
## The chat history is maintained in a list, which is updated with each user input and AI response.


import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
