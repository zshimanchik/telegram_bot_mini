import requests

class TelegramApiException(Exception):
    pass


class BotWasBlockedException(TelegramApiException):
    pass


class TelegramBotApi:
    def __init__(self, token):
        self._token = token
        self.base_url = 'https://api.telegram.org/bot{}'.format(token)

    def send_message(self, chat_id, message, keyboard=None):
        data = {"text": message, "chat_id": chat_id}
        if keyboard is not None:
            data['reply_markup'] = {"keyboard": keyboard}
        url = self.base_url + "/sendMessage"
        self._send_request(url, data)

    def send_photo(self, chat_id, photo, keyboard=None):
        data = {"photo": photo, "chat_id": chat_id}
        if keyboard is not None:
            data['reply_markup'] = {"keyboard": keyboard}
        url = self.base_url + "/sendPhoto"
        self._send_request(url, data)

    def _send_request(self, url, data):
        response = requests.post(url, json=data)
        if response.status_code == 403 and 'bot was blocked' in response.text:
            raise BotWasBlockedException()
        response.raise_for_status()
