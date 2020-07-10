
import os
import sys
import requests
import datetime
from pprint import pprint

import config
import utils
import sendline
import sendtwitter

# 引数を受け取る
if (len(sys.argv) > 1):

    caller = sys.argv[1] # 呼び出し元のバッチファイルの名前
    print('引数: ' + caller)

    if (caller in config.NOTIFY_MESSAGE):

        # メッセージをセット
        message = str(datetime.datetime.now()) + ': ' + config.NOTIFY_MESSAGE[caller]

    else:

        # 引数が不正なので終了    
        print('引数が不正です。')
        sys.exit(1)

else:

    # 引数がないので終了    
    print('引数がありません。')
    sys.exit(1)

print(os.environ)

# マクロを取得
macros = utils.get_macro(os.environ)

# マクロでメッセージを置換
for macro, macro_value in macros.items():

    # $$ で囲われた文字を置換する
    message = message.replace('$' + macro + '$', macro_value)


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

    line = sendline.Line(config.LINE_ACCESS_TOKEN)

    result_line = line.send_message(message, image = image)

    print(result_line)

# Twitter にメッセージを送信
if (config.NOTIFY_TYPE == 'ALL' or config.NOTIFY_TYPE == 'Twitter'):

    twitter = sendtwitter.Twitter(
        config.TWITTER_CONSUMER_KEY, 
        config.TWITTER_CONSUMER_SECRET, 
        config.TWITTER_ACCESS_TOKEN, 
        config.TWITTER_ACCESS_TOKEN_SECRET
    )

    if (config.NOTIFY_TWITTER_TYPE == 'Tweet'):

        # ツイートで送信
        result_twitter = twitter.send_tweet(message, image = image)

    elif (config.NOTIFY_TWITTER_TYPE == 'DirectMessage'):

        # ダイレクトメッセージで送信
        result_twitter = twitter.send_direct_message(message, image = image, destination = config.NOTIFY_TWITTER_DESTINATION)

    print(result_twitter)
