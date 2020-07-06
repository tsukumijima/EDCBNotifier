
# Twitter でメッセージを送信する

import os
from twitter import Twitter as TwitterTool
from twitter import OAuth

class Twitter:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):

        # 初期化
        self.twitter = TwitterTool(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        self.upload = TwitterTool(domain = 'upload.twitter.com', auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

    def sendMessage(self, message, image = None):

        if (image != None and os.path.isfile(image)) :

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
