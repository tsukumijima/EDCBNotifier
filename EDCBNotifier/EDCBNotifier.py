
import os
import sys
import datetime
import requests
from pprint import pprint

import config
import utils
from sendline import Line
from sendtwitter import Twitter


def main():

    # ヘッダー
    header = '+' * 60 + '\n'
    header += '+{:^58}+\n'.format('EDCBNotifier version ' + utils.get_version())
    header += '+' * 60 + '\n'
    print('\n' + header)

    print('Time: ' + str(datetime.datetime.now()), end = '\n\n')


    # 引数を受け取る
    if (len(sys.argv) > 1):

        caller = sys.argv[1] # 呼び出し元のバッチファイルの名前
        print('Param: ' + caller, end = '\n\n')

        if (caller in config.NOTIFY_MESSAGE):

            # メッセージをセット
            message = config.NOTIFY_MESSAGE[caller]

        else:

            # 引数が不正なので終了    
            utils.error('Error: Invalid argument.')

    else:

        # 引数がないので終了
        utils.error('Error: Argument does not exist.')


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


    print('Message: ' + message.replace('\n', '\n         '), end = '\n\n')


    # LINE Notify にメッセージを送信
    if ('LINE' in config.NOTIFY_TYPE):

        line = Line(config.LINE_ACCESS_TOKEN)

        try:
            result_line = line.send_message(message, image = image)
        except Exception as error:
            result_line_print = 'Error: ' + error.args[0]
        else:
            if result_line['status'] != 200:
                # ステータスが 200 以外（失敗）
                result_line_print = 'Error: ' + result_line['message']
            else:
                # ステータスが 200（成功）
                result_line_print = 'Message: ' + result_line['message']

            print('[LINE Notify] Status Code: ' + str(result_line['status']))

        print('[LINE Notify] ' + result_line_print, end = '\n\n')


    # Twitter にツイートを送信
    if ('Tweet' in config.NOTIFY_TYPE):

        twitter = Twitter(
            config.TWITTER_CONSUMER_KEY,
            config.TWITTER_CONSUMER_SECRET,
            config.TWITTER_ACCESS_TOKEN,
            config.TWITTER_ACCESS_TOKEN_SECRET
        )

        # ツイートを送信
        try:
            result_tweet = twitter.send_tweet(message, image = image)
        except Exception as error:
            print('[Tweet] Result: Failed')
            print('[Tweet] Error: ' + error.args[0], end = '\n\n')
        else:
            print('[Tweet] Result: Success')
            print('[Tweet] Tweet: https://twitter.com/i/status/' + str(result_tweet['id']), end = '\n\n')


    # Twitter にダイレクトメッセージを送信
    if ('DirectMessage' in config.NOTIFY_TYPE):

        twitter = Twitter(
            config.TWITTER_CONSUMER_KEY,
            config.TWITTER_CONSUMER_SECRET,
            config.TWITTER_ACCESS_TOKEN,
            config.TWITTER_ACCESS_TOKEN_SECRET
        )

        # ダイレクトメッセージを送信
        try:
            result_directmessage = twitter.send_direct_message(message, image = image, destination = config.NOTIFY_DIRECTMESSAGE_TO)
        except Exception as error:
            print('[DirectMessage] Result: Failed')
            print('[DirectMessage] Error: ' + error.args[0], end = '\n\n')
        else:
            print('[DirectMessage] Result: Success')
            print('[DirectMessage] Message: https://twitter.com/messages/' + 
                result_directmessage['event']['message_create']['target']['recipient_id'] + '-' +
                result_directmessage['event']['message_create']['sender_id'], end = '\n\n')


if __name__ == '__main__':
    main()
