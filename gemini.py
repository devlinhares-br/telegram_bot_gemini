import google.generativeai as genai
from os import getenv

class Gemini_api():

    def __init__(self) -> None:
        genai.configure(api_key=getenv("token_gg"))
        self.model = genai.GenerativeModel('gemini-pro')
        pass

    def send_message(self, message:str)-> str:
        

        response = self.model.generate_content(message)
        print('Gemini:\n')
        print(response.text)
        return (response.text)
