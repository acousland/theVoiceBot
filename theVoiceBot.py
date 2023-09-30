from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
import openai
import streamlit as st
import prompts

st.title("The Voice Bot")
#st.warning('TheVoiceBot will not capture any data entered  ', icon="⚠️")
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
  st.session_state["messages"] = [ChatMessage(role="system", content=setupPrompt)]
  st.session_state.messages.append(ChatMessage(role="assistant", content="OK let's talk about the voice. I'm going to ask you a series of questions. Answer as if there was a person on the other side, and then I'll give you a indication where you fit on the spectrum of views. Is now a good time for you?"))

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
                         #model = "gpt-3.5-turbo-0613",
                         model = "gpt-4",
                         callbacks=[stream_handler])
        response = llm(st.session_state.messages)
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
