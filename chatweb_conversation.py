import streamlit as st
from configure import get_key as g
from settings import generation_config,safety_settings
from IPython.display import display
from IPython.display import Markdown
import textwrap as t


import google.generativeai as genai

print('the key is ',g())
genai.configure(api_key=g())
model=genai.GenerativeModel(model_name='gemini-1.5-flash',
                            generation_config=generation_config,
                            safety_settings=safety_settings)
chat=model.start_chat(history=[])

# function to load the model and get response
def get_gemini_response(question):    
    response=chat.send_message(question,stream=True)
    return response   

    
st.set_page_config(page_title="Q&A Project with Memory")
st.header("Google Gemini Application")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
i=st.text_input("Input: ",key="mama")
submit=st.button('Ask The Question!!!')

if submit and i:
        response=get_gemini_response(i)
        # Add user query and response to session state of Streamlit
        st.session_state['chat_history'].append(("You",i))
        st.subheader('The Response is ....')
        for chunck in response:
            st.write(chunck.text)
            st.session_state['chat_history'].append(("ChatBot",chunck.text))
    
st.subheader('The Chat History is ')
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")



    


