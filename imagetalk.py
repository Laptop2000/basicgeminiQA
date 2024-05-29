from configure import get_key as g
from settings import generation_config,safety_settings
from PIL import Image

import google.generativeai as genai

print('the key is ',g())

genai.configure(api_key=g())

model=genai.GenerativeModel(model_name='gemini-1.5-flash',
                            generation_config=generation_config,
                            safety_settings=safety_settings)



image=input('\n Enter an Image Path.... \n')
img=Image.open(image)

def talk_to_me():
     response=model.generate_content([input('\n enter your image realted query \n'),img])
     print(response.text)

talk_to_me()







