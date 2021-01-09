from telepotpro import Bot
from time import sleep
from threading import Thread
from pony.orm import db_session

from modules.api import GeometryDashApi, ApiRequestError
from modules.database import User

try:
    f = open('token.txt', 'r')
    token = f.readline().strip()
    f.close()
except FileNotFoundError:
    token = input(" * Paste here the API Token: ")
    f = open('token.txt', 'w')
    f.write(token)
    f.close()

bot = Bot(token)
api = GeometryDashApi()


@db_session
def reply(msg):
    chatId = msg['from']['id']
    text = msg['text']
    name = msg['from']['first_name']

    if not User.exists(lambda u: u.chatId == chatId):
        User(chatId=chatId)

    user = User.get(chatId=chatId)

    if text.startswith("/geticon"):
        params = text.split(2)
        bot.sendPhoto(chatId, api.getIcon(params[1], params[2] if len(params) > 2 else None))
    else:
        bot.sendMessage(chatId, "Hey, <b>{}</b>!\nThis bot is still under development, check later...".format(name), parse_mode="HTML")


def accept_message(msg):
    Thread(target=reply, args=[msg]).start()

bot.message_loop({'chat': accept_message})


while True:
    sleep(60)
