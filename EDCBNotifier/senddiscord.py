
# Discord でメッセージを送信する

import os
import requests
import json

class Discord:

    def __init__(self, webhook_url):

        self.webhook_url = webhook_url
        # print(self.webhook_url)

    # メッセージを送信する
    def send_message(self, message, image = None):

        url = self.webhook_url
        headers = {
            'Content-Type': 'application/json' 
         }


        # メッセージ
        payload = {
            'username':'EDCBNotifier',
            'avatar_url': 'https://github.com/tsukumijima/EDCBNotifier/blob/master/EDCBNotifier/EDCBNotifier.png?raw=true',
            'content': message
        }

       #画像送信ロジックは未実装
        #if image != None and os.path.isfile(image):

            # 画像とテキストを送信
        #    files = {'imageFile': open(image, 'rb')}
        #    response = requests.post(url, json.dumps(payload), headers = headers, files = files)

        #else:

            # テキストのみ送信
        response = requests.post(url, json.dumps(payload), headers = headers)
        response_res = str(response) #検索するときに不都合なので文字列に変換

        # json を返す
        # DiscordはResponseの中身がない204を返すので自分で疑似的にResponseを生成する
        if '204' in response_res :
            response.json = json.loads('{"status":204,"message":"Successfully"}')
        else :
            response.json = json.loads('{"status":400,"message":"Send Faild"}')

        return response.json

