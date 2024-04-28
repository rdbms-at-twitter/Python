import time
import boto3
import base64
import streamlit as st

from langchain_aws.chat_models import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


st.title("Amazon Bedrock Image Analyzer")

# Setup bedrock connection
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

# Set up bedrock basic option for the medel
@st.cache_resource
def load_chat():
    chat = ChatBedrock(
        client=bedrock_runtime,
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
        model_kwargs = {"temperature": 0.0}
    )

    return chat

st.write('Please upload image for analyzing contents.')

chat = load_chat()

uploaded_file = st.file_uploader("Image", type="jpg")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Please tell me what kind of information should I check?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        content = []


        if uploaded_file:
            image_data = base64.b64encode(uploaded_file.read()).decode('utf-8')
            content.append(
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data
                    }
                }
            )
    
        content.append(
            {
                "type": "text",
                "text": prompt
            }
        )

        messages = [
            HumanMessage(
                content=content
            )
        ]

        # prompt = prompt_fixer(prompt)
        result = chat.invoke(messages)

        # Simulate stream of response with milliseconds delay
        for chunk in result.content.split(' '): 
            full_response += chunk + ' '
            if chunk.endswith('\n'):
                full_response += ' '
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
