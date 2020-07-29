
# Twitter でメッセージを送信する

import os
import twitter

class Twitter:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):

        # 初期化
        self.twitter = twitter.Twitter(auth = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        self.upload = twitter.Twitter(domain = 'upload.twitter.com', auth = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        
        # 自分の情報を取得
        self.accountinfo = self.twitter.account.verify_credentials()

    # ツイートを送信する
    def send_tweet(self, message, image = None):

        if (image != None and os.path.isfile(image)):

            # 画像を読み込み
            with open(image, 'rb') as imagefile:

                imagedata = imagefile.read()

            # 画像をアップロードして media_id を取得
            media_id = self.upload.media.upload(media = imagedata)['media_id_string']

            # 画像とテキストを送信
            response = self.twitter.statuses.update(status = message, media_ids = media_id)

        else:

            # テキストのみ送信
            response = self.twitter.statuses.update(status = message)

        # レスポンスを返す
        return response

    # ダイレクトメッセージを送信する
    def send_direct_message(self, message, image = None, destination = None):

        if (destination == None):

            # 自分自身のID
            recipient_id = self.accountinfo['id']

        else:

            # スクリーンネームからIDを取得する
            recipient_id = self.twitter.users.show(screen_name = destination)['id']

        if (image != None and os.path.isfile(image)):

            # 画像を読み込み
            with open(image, 'rb') as imagefile:

                imagedata = imagefile.read()

            # 画像をアップロードして media_id を取得
            media_id = self.upload.media.upload(media = imagedata)['media_id_string']

            # 画像とテキストを送信
            # 新 API になって仕様が変わったらしい
            response = self.twitter.direct_messages.events.new(_json = {
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
            response = self.twitter.direct_messages.events.new(_json = {
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

        # レスポンスを返す
        return response
