
import io
import json
import os
import requests


class Discord:
    """
    Discord の Webhook でメッセージを送信するクラス
    """

    def __init__(self, webhook_url:str):
        """
        Args:
            webhook_url (str): Discord の Webhook の URL
        """

        self.webhook_url = webhook_url


    def sendMessage(self, message:str, image_path:str=None) -> dict:
        """
        Discord の Webhook でメッセージを送信する

        Args:
            message (str): 送信するメッセージの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: ステータスコードとエラーメッセージが入った辞書
        """

        # リクエストヘッダー
        # 公式ドキュメントいわく、画像も一緒に送る場合は multipart/form-data である必要があるらしい
        # ref: https://discord.com/developers/docs/resources/channel#create-message
        headers = {
            'Content-Type': 'multipart/form-data',
        }

        # メッセージ
        payload = {
            'username':'EDCBNotifier',
            'avatar_url': 'https://raw.githubusercontent.com/tsukumijima/EDCBNotifier/master/EDCBNotifier/EDCBNotifier.png',
            'content': message,
        }

        # 送信するファイル
        # ref: https://qiita.com/bgcanary/items/6d81b7813434978362f4
        files = {
            'payload_json': ('request.json', io.BytesIO(json.dumps(payload).encode('utf-8')), 'application/json')
        }

        # 送信するファイルに画像を追加
        if image_path is not None and os.path.isfile(image_path):
            files['files[0]'] = (os.path.basename(image_path), open(image_path, 'rb'))

        # Webhook を送信
        response = requests.post(self.webhook_url, headers=headers, files=files)

        # 失敗した場合はエラーメッセージを取得
        if response.status_code != 204:
            message = response.json()['message'] + f' (Code:{response.json()["code"]})'
        else:
            message = 'Success'

        # ステータスコードとエラーメッセージを返す
        return {
            'status': response.status_code,
            'message': message,
        }
