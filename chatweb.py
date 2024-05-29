import streamlit as st
from configure import get_key as g
from settings import generation_config,safety_settings
from IPython.display import display
from IPython.display import Markdown
import textwrap as t


import google.generativeai as genai

print('the key is ',g())
genai.configure(api_key=g())




# function to load the model and get response
def get_gemini_response(question):
    model=genai.GenerativeModel(model_name='gemini-1.5-flash',
                            generation_config=generation_config,
                            safety_settings=safety_settings)
    response=model.generate_content(question)
    return response.text
    

    
st.set_page_config(page_title="Q&A Project")
st.header("Google Gemini Application")
i=st.text_input("Input: ",key="mama")
submit=st.button('Ask The Question!!!')

if submit:
    response=get_gemini_response(i)
    st.subheader('The Response is ....')
    st.write(response)



