
import os
import requests
import datetime
from pprint import pprint

import config
import send_line
import send_twitter

message = str(datetime.datetime.now()) + ': EDCBNotifier のテストです'

print(message)

# LINE Notify にメッセージを送信
if (config.NOTIFY_TYPE == 'ALL' or config.NOTIFY_TYPE == 'LINE') :

    line = send_line.Line(config.LINE_ACCESS_TOKEN)

    result_line = line.sendMessage(message)

    print(result_line)

# Twitter にメッセージを送信
if (config.NOTIFY_TYPE == 'ALL' or config.NOTIFY_TYPE == 'Twitter') :

    twitter = send_twitter.Twitter(
        config.TWITTER_CONSUMER_KEY, 
        config.TWITTER_CONSUMER_SECRET, 
        config.TWITTER_ACCESS_TOKEN, 
        config.TWITTER_ACCESS_TOKEN_SECRET
    )

    result_twitter = twitter.sendMessage(message)

    print(result_twitter)
