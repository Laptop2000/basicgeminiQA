import os
from dotenv import load_dotenv,find_dotenv

def get_key():
    status=load_dotenv(find_dotenv(),override=True)
    print('file found ',status)
    return os.environ.get("GOOGLE_API_KEY")