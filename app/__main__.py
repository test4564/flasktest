import threading
import os

from app import bot

from flask import Flask
from pyrogram import idle
from waitress import serve

web = Flask(__name__)

@web.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@web.route('/test')
def test():
    bot.send_message(chat_id='@hawardwolowitzs', text='Hey there!')
    return 'Test'

# threading.Thread(target=web.run, daemon=True).start()
# bot.start()
# idle()

def web_main():
    serve(web, port=5000)

if __name__ == '__main__':
    print('Starting bot')
    # start waitress in a thread and idle pyrogram in main thread
    port = int(os.environ.get('PORT', 5000))
    threading.Thread(target=web_main, daemon=True).start()
    bot.start()
    idle()
