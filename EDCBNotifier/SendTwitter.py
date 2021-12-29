
import os
import twitter


class Twitter:
    """
    Twitter でメッセージを送信する
    """

    def __init__(self, consumer_key:str, consumer_secret:str, access_token:str, access_token_secret:str):
        """
        Args:
            consumer_key (str): Twitter API のコンシューマーキー
            consumer_secret (str): Twitter API のコンシューマーシークレット
            access_token (str): Twitter API のアクセストークン
            access_token_secret (str): Twitter API のアクセストークンシークレット
        """

        # 初期化
        self.oauth = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
        self.twitter = twitter.Twitter(auth=self.oauth)
        self.upload = twitter.Twitter(domain='upload.twitter.com', auth=self.oauth)

        # 自分の情報を取得
        self.account_info = self.twitter.account.verify_credentials()


    def sendTweet(self, message:str, image_path:str=None) -> dict:
        """
        ツイートを送信する

        Args:
            message (str): 送信するツイートの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: API レスポンスのデータ
        """

        if (image_path is not None and os.path.isfile(image_path)):

            # 画像を読み込み
            with open(image_path, 'rb') as image_file:

                image_data = image_file.read()

            # 画像をアップロードして media_id を取得
            media_id = self.upload.media.upload(media=image_data)['media_id_string']

            # 画像とテキストを送信
            response = self.twitter.statuses.update(status=message, media_ids=media_id)

        else:

            # テキストのみ送信
            response = self.twitter.statuses.update(status=message)

        # API レスポンスを返す
        return response


    def sendDirectMessage(self, message:str, destination:str=None, image_path:str=None) -> dict:
        """
        ダイレクトメッセージを送信する

        Args:
            message (str): 送信するダイレクトメッセージの本文
            destination (str, optional): ダイレクトメッセージを送信するアカウントのスクリーンネーム. Defaults to None.
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: API レスポンスのデータ
        """

        if (destination is None):

            # 自分自身のID
            recipient_id = self.account_info['id']

        else:

            # スクリーンネームからIDを取得する
            recipient_id = self.twitter.users.show(screen_name=destination)['id']

        if (image_path is not None and os.path.isfile(image_path)):

            # 画像を読み込み
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()

            # 画像をアップロードして media_id を取得
            media_id = self.upload.media.upload(media=image_data)['media_id_string']

            # 画像とテキストを送信
            # 新 API になって仕様が変わったらしい
            response = self.twitter.direct_messages.events.new(_json={
                'event': {
                    'type': 'message_create',
                    'message_create': {
                        'target': {
                            'recipient_id': recipient_id
                        },
                        'message_data': {
                            'text': message,
                            'attachment': {
                                'type': 'media',
                                'media': {
                                    'id': media_id
                                }
                            }
                        }
                    }
                }
            })

        else:

            # テキストのみ送信
            response = self.twitter.direct_messages.events.new(_json={
                'event': {
                    'type': 'message_create',
                    'message_create': {
                        'target': {
                            'recipient_id': recipient_id
                        },
                        'message_data': {
                            'text': message
                        }
                    }
                }
            })

        # API レスポンスを返す
        return response
