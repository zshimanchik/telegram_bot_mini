import logging

from flask import Flask, request

from telegram_bot_mini.bot import Bot
from telegram_bot_mini.bot_api import TelegramBotApi

_LOGGER = logging.getLogger(__name__)
WEBHOOK_TOKEN = 'longsecuretoken'
app = Flask(__name__)
bot_api = TelegramBotApi('123456789:ABCDEFGH123456-12345678912345678912')
bot = Bot(bot_api)


@app.route(f'/tg/{WEBHOOK_TOKEN}', methods=['POST'])
def telegram_webhook():
    content = request.get_json()
    bot.handle_update(content)
    return 'OK'


@bot.command('/start', '')
def start(api: TelegramBotApi, update):
    first_name = update['message']['from'].get('first_name', '%username%')
    api.send_message(update['message']['chat']['id'], f'Hello {first_name}!')


@bot.command('/whoami', '/whoami - show info about your account')
def whoami(api: TelegramBotApi, update):
    name = update['message']['from'].get('first_name') or update['message']['from'].get('username')
    api.send_message(update['message']['chat']['id'], f'You are: {name}')


@bot.command('/say', '/say <text> - reply with text')
def whoami(api: TelegramBotApi, update):
    reply_text = update['message']['text'][len('/say'):].strip()
    if not reply_text:
        reply_text = 'You should add text'
    api.send_message(update['message']['chat']['id'], reply_text)


@bot.fallback
def fallback(api: TelegramBotApi, update):
    api.send_message(update['message']['chat']['id'], 'I cant understand. Use /help')


@bot.error
def error(api: TelegramBotApi, update, exception):
    _LOGGER.exception("Error handler was invoked. Error: '%s', update: '%s'", exception, update, exc_info=exception)
    api.send_message(update['message']['chat']['id'], 'Oops. There is an error')


bot.generate_and_add_help_command('Available commands:', '/help - shows this message')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
