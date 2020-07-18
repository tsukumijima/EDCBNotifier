
# LINE Notify でメッセージを送信する

import os
import requests

class Line:

    def __init__(self, access_token):

        self.access_token = access_token

    # メッセージを送信する
    def send_message(self, message, image = None):

        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + self.access_token}

        # メッセージ
        payload = {'message': message}

        if image != None and os.path.isfile(image):

            # 画像とテキストを送信
            files = {'imageFile': open(image, 'rb')}
            response = requests.post(url, headers = headers, params = payload, files = files)

        else:

            # テキストのみ送信
            response = requests.post(url, headers = headers, params = payload)

        # print(response)
        # print(response.json())

        # json を返す
        return response.json()
