from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
import openai
import streamlit as st
import prompts.prompts as prompts
import prompts.sourceMaterial as sourceMaterial

# Open and read the 'header.md' file, and store its content in the 'body' variable.
with open('copy/header.md', 'r') as f:
    body = f.read()

# Display header icon of robot Emu and Kangaroo
st.image('assets/header_icon.png', width=150)

# Render the content of 'body' as Markdown.
st.markdown(body, unsafe_allow_html=False, help=None)

# Combine prompts to create the setup prompt.
setupPrompt = prompts.botDirectionsPrompt + prompts.enquiryLinesPrompt

# Create a StreamHandler class to handle the streaming of new tokens to give the effect of typing when the LLM is responding
class StreamHandler(BaseCallbackHandler):
  def __init__(self, container, initial_text=""):
    self.container = container
    self.text = initial_text

  def on_llm_new_token(self, token: str, **kwargs) -> None:
    self.text += token
    self.container.markdown(self.text)

# Check if API key is stored in session state, if not, get it from secrets.
if openai.api_key not in st.session_state:
  openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize chat messages if not already present in the session state.
if "messages" not in st.session_state:
  # Load initial system messages into the chat.
  st.session_state["messages"] = [ChatMessage(role="system", content=sourceMaterial.noSummary)]
  st.session_state["messages"] = [ChatMessage(role="system", content=sourceMaterial.yesSummary)]
  st.session_state["messages"] = [ChatMessage(role="system", content=setupPrompt)]
  
  # Load assistant’s welcome messages into the chat.
  st.session_state.messages.append(ChatMessage(role="assistant", content=prompts.welcomePrompt))
  st.session_state.messages.append(ChatMessage(role="assistant", content="Ready to start?"))

# Display existing chat messages.
for msg in st.session_state.messages:
    if (msg.role == "assistant" or msg.role == "user"):
      st.chat_message(msg.role).write(msg.content)

# Accept user input and display it in the chat.
if prompt := st.chat_input():
    
    # Append the user’s message to the session state.
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    # Handle assistant’s response.
    with st.chat_message("assistant"):
        # Create a stream handler to display the assistant’s response.
        stream_handler = StreamHandler(st.empty())

         # Create a ChatOpenAI object to generate the assistant’s response.
        llm = ChatOpenAI(openai_api_key=openai.api_key, 
                         streaming=True, 
                         model = "gpt-4",
                         callbacks=[stream_handler])
        
        # Generate and display the assistant's response
        response = llm(st.session_state.messages)
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
