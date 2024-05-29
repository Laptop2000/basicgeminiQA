from configure import get_key as g
from settings import generation_config,safety_settings

import google.generativeai as genai

print('the key is ',g())

genai.configure(api_key=g())

model=genai.GenerativeModel(model_name='gemini-1.5-flash',
                            generation_config=generation_config,
                            safety_settings=safety_settings)

def show_models():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
                print(m)

def talk_to_me(prompt):
     response=model.generate_content(prompt)
     print(response.text)


talk_to_me(input("\n Enter your question \n"))






