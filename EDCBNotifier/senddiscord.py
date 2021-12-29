
# Discord でメッセージを送信する

import requests
import json

class Discord:

    def __init__(self, webhook_url):

        self.webhook_url = webhook_url

    # メッセージを送信する
    def send_message(self, message, image = None):

        headers = {
            'Content-Type': 'application/json',
        }

        # メッセージ
        payload = {
            'username':'EDCBNotifier',
            'avatar_url': 'https://github.com/tsukumijima/EDCBNotifier/blob/master/EDCBNotifier/EDCBNotifier.png?raw=true',
            'content': message,
        }

        # テキストのみ送信
        response = requests.post(self.webhook_url, json.dumps(payload), headers = headers)
        response_res = str(response) #検索するときに不都合なので文字列に変換

        # json を返す
        # DiscordはResponseの中身がない204を返すので自分で疑似的にResponseを生成する
        if '204' in response_res :
            response.json = json.loads('{"status":204,"message":"Successfully"}')
        else :
            response.json = json.loads('{"status":400,"message":"Send Faild"}')

        return response.json
