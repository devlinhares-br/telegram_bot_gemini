from dotenv import load_dotenv
from tele import Telegram_bot
from gemini import Gemini_api
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

telegram = Telegram_bot()
gemini = Gemini_api()

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    msg = request.get_json()
    print(msg)
    g_response = gemini.send_message(msg['message']['text'])
    telegram.send_message(g_response, msg['message']['chat']['id'])
    return '200'



if '__main__' == __name__:
    app.run()