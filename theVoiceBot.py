from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
import openai
import streamlit as st
import prompts
import sourceMaterial
import time


with open('header.md', 'r') as f:
    body = f.read()

st.image('assets/header_icon.png', width=150)

st.markdown(body, unsafe_allow_html=False, help=None)

setupPrompt = prompts.botDirectionsPrompt + prompts.enquiryLinesPrompt

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

if openai.api_key not in st.session_state:
  openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
  st.session_state["messages"] = [ChatMessage(role="system", content=sourceMaterial.noSummary)]
  st.session_state["messages"] = [ChatMessage(role="system", content=sourceMaterial.yesSummary)]
  st.session_state["messages"] = [ChatMessage(role="system", content=setupPrompt)]
  st.session_state.messages.append(ChatMessage(role="assistant", content=prompts.welcomePrompt))  
  st.session_state.messages.append(ChatMessage(role="assistant", content="I've been trained on the voice yes/no document from the AEC only, so I don't know about viewpoints and arguments not presented in those. Feel free to raise any other arguments while we chat and I'll incorporate those."))
  st.session_state.messages.append(ChatMessage(role="assistant", content="Ready to start?"))

for msg in st.session_state.messages:
    if (msg.role == "assistant" or msg.role == "user"):
      st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOpenAI(openai_api_key=openai.api_key, 
                         streaming=True, 
                         model = "gpt-4",
                         callbacks=[stream_handler])
        response = llm(st.session_state.messages)
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
