from os import getenv
import requests



class Telegram_bot():

    
    
    def __init__(self) -> None:
        TOKEN = getenv('token_tl')
        self.BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'
        pass

    def send_message(self, message, chat_id):
        url = f'{self.BASE_URL}sendMessage'
        print(url)
        params = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.get(url, params=params)
        print('telegra:m \n')
        print(chat_id)
        print(response.json())
        return response.json()
