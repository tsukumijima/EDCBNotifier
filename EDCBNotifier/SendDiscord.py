
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


    def sendMessage(self, message:str, image_path:str=None) -> int:
        """
        Discord の Webhook でメッセージを送信する

        Args:
            message (str): 送信するメッセージの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            int: API レスポンスのステータスコード
        """

        # リクエストヘッダー
        headers = {
            'Content-Type': 'application/json',
        }

        # メッセージ
        payload = {
            'username':'EDCBNotifier',
            'avatar_url': 'https://raw.githubusercontent.com/tsukumijima/EDCBNotifier/master/EDCBNotifier/EDCBNotifier.png',
            'content': message,
        }

        # テキストのみ送信
        response = requests.post(self.webhook_url, headers=headers, params=payload)

        # ステータスコードを返す
        # Discord の Webhook は基本 204 (No Content) を返すため
        return response.status_code
