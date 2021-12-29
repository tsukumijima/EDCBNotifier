
import os
import requests


class LINE:
    """
    LINE Notify でメッセージを送信するクラス
    """

    def __init__(self, access_token:str):
        """
        Args:
            access_token (str): LINE Notify のアクセストークン
        """

        self.access_token = access_token


    def sendMessage(self, message:str, image_path:str=None) -> dict:
        """
        LINE Notify でメッセージを送信する

        Args:
            message (str): 送信するメッセージの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: API レスポンスのデータ
        """

        # LINE Notify の API
        url = 'https://notify-api.line.me/api/notify'

        # リクエストヘッダー
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
        }

        # メッセージ
        payload = {
            'message': message,
        }

        if image_path is not None and os.path.isfile(image_path):

            # 画像とテキストを送信
            image_data = {'imageFile': open(image_path, 'rb')}
            response = requests.post(url, headers=headers, data=payload, files=image_data)

        else:

            # テキストのみ送信
            response = requests.post(url, headers=headers, data=payload)

        # API レスポンスを返す
        return response.json()
