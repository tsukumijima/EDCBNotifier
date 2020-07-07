
import os
import requests
import datetime
from pprint import pprint

import config
import send_line
import send_twitter

message = str(datetime.datetime.now()) + ': EDCBNotifier のテストです'

# 送信する画像
if (config.NOTIFY_IMAGE != None and os.path.isfile(config.NOTIFY_IMAGE)):

    # そのまま使う
    image = config.NOTIFY_IMAGE

elif (config.NOTIFY_IMAGE != None and os.path.isfile(os.path.dirname(__file__) + '/' + config.NOTIFY_IMAGE)):

    # パスを取得して連結
    image = os.path.dirname(__file__) + '/' + config.NOTIFY_IMAGE

else:

    # 画像なし
    image = None

print(message)

# LINE Notify にメッセージを送信
if (config.NOTIFY_TYPE == 'ALL' or config.NOTIFY_TYPE == 'LINE'):

    line = send_line.Line(config.LINE_ACCESS_TOKEN)

    result_line = line.sendMessage(message, image = image)

    print(result_line)

# Twitter にメッセージを送信
if (config.NOTIFY_TYPE == 'ALL' or config.NOTIFY_TYPE == 'Twitter'):

    twitter = send_twitter.Twitter(
        config.TWITTER_CONSUMER_KEY, 
        config.TWITTER_CONSUMER_SECRET, 
        config.TWITTER_ACCESS_TOKEN, 
        config.TWITTER_ACCESS_TOKEN_SECRET
    )

    if (config.NOTIFY_TWITTER_TYPE == 'Tweet'):

        # ツイートで送信
        result_twitter = twitter.sendTweet(message, image = image)

    elif (config.NOTIFY_TWITTER_TYPE == 'DirectMessage'):

        # ダイレクトメッセージで送信
        result_twitter = twitter.sendDirectMessage(message, image = image, destination = config.NOTIFY_TWITTER_DESTINATION)

    print(result_twitter)
