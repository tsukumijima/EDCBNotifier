
import colorama
import os
import shutil
import sys

import config
from SendDiscord import Discord
from SendLINE import LINE
from SendTwitter import Twitter
from Utils import Utils

# バージョン情報
__version__ = '1.2.0'


def main():

    # このファイルが存在するフォルダの絶対パス
    current_folder = os.path.dirname(os.path.abspath(sys.argv[0]))

    # ターミナルの横幅
    # conhost.exe だと -1px しないと改行されてしまう
    terminal_columns = shutil.get_terminal_size().columns - 1

    # 初期化
    colorama.init(autoreset=True)
    if config.NOTIFY_LOG:  # 標準出力をファイルに変更
        sys.stdout = open(current_folder + '/EDCBNotifier.log', mode='w', encoding='utf-8')
        sys.stderr = open(current_folder + '/EDCBNotifier.log', mode='w', encoding='utf-8')

    # ヘッダー
    print('=' * terminal_columns)
    print(f'+++++{f"EDCBNotifier version {__version__}":^{terminal_columns - 10}}+++++')
    print('=' * terminal_columns)

    # 引数を受け取る
    if len(sys.argv) > 1:

        # 呼び出し元のイベント
        caller = sys.argv[1]  # 呼び出し元のバッチファイルの名前
        print(f'Event: {caller}')

        # 実行時刻
        print(f'Execution Time: {Utils.getExecutionTime()}')

        # NOTIFY_MESSAGE にあるイベントでかつ通知がオンになっていればメッセージをセット
        if (caller in config.NOTIFY_MESSAGE and caller in config.NOTIFY_EVENT):
            message = config.NOTIFY_MESSAGE[caller]

        # NOTIFY_MESSAGE にあるイベントだが、通知がオフになっているので終了
        elif caller in config.NOTIFY_MESSAGE:
            print(f'Info: {caller} notification is off, so it ends.')
            print('=' * terminal_columns)
            sys.exit(0)

        # 引数が不正なので終了
        else:
            Utils.error('Invalid argument.')

    # 引数がないので終了
    else:
        Utils.error('Argument does not exist.')

    print('-' * terminal_columns)

    # マクロを取得
    macros = Utils.getMacro(os.environ)
    # メッセージを置換
    for macro, macro_value in macros.items():
        # $$ で囲われた文字を置換する
        message = message.replace(f'${macro}$', macro_value)

    print('Message: ' + message.replace('\n', '\n         '))

    # 送信する画像
    # パスをそのまま利用
    if (config.NOTIFY_IMAGE is not None) and (os.path.isfile(config.NOTIFY_IMAGE)):
        image = config.NOTIFY_IMAGE

    # パスを取得して連結
    elif (config.NOTIFY_IMAGE is not None) and (os.path.isfile(current_folder + '/' + config.NOTIFY_IMAGE)):
        image = current_folder + '/' + config.NOTIFY_IMAGE

    # 画像なし
    else:
        image = None

    # LINE Notify にメッセージを送信
    if 'LINE' in config.NOTIFY_TYPE:

        print('-' * terminal_columns)

        line = LINE(config.LINE_ACCESS_TOKEN)

        try:
            result_line:dict = line.sendMessage(message, image_path=image)
        except Exception as error:
            print(f'[LINE Notify] Result: Failed')
            print(f'[LINE Notify] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            if result_line['status'] != 200:
                # ステータスが 200 以外（失敗）
                print(f'[LINE Notify] Result: Failed (Code: {result_line["status"]})')
                print(f'[LINE Notify] {colorama.Fore.RED}Error: {result_line["message"]}')
            else:
                # ステータスが 200（成功）
                print(f'[LINE Notify] Result: Success (Code: {result_line["status"]})')
                print(f'[LINE Notify] Message: {result_line["message"]}')

    # Discord にメッセージを送信
    if 'Discord' in config.NOTIFY_TYPE:

        print('-' * terminal_columns)

        discord = Discord(config.Discord_WEBHOOK_URL)

        try:
            result_discord:dict = discord.sendMessage(message, image_path=image)
        except Exception as error:
            print(f'[Discord] Result: Failed')
            print(f'[Discord] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            if result_discord['status'] != 200 and result_discord['status'] != 204:
                # ステータスが 200 or 204 以外（失敗）
                print(f'[Discord] Result: Failed (Code: {result_discord["status"]})')
                print(f'[Discord] {colorama.Fore.RED}Error: {result_discord["message"]}')
            else:
                # ステータスが 200 or 204（成功）
                print(f'[Discord] Result: Success (Code: {result_discord["status"]})')
                print(f'[Discord] Message: {result_discord["message"]}')

    # Twitter API を初期化
    if 'Tweet' in config.NOTIFY_TYPE or 'DirectMessage' in config.NOTIFY_TYPE:

        twitter = Twitter(
            config.TWITTER_CONSUMER_KEY,
            config.TWITTER_CONSUMER_SECRET,
            config.TWITTER_ACCESS_TOKEN,
            config.TWITTER_ACCESS_TOKEN_SECRET
        )

    # Twitter にツイートを送信
    if 'Tweet' in config.NOTIFY_TYPE:

        print('-' * terminal_columns)

        # ツイートを送信
        try:
            result_tweet:dict = twitter.sendTweet(message, image_path=image)
        except Exception as error:
            print(f'[Tweet] Result: Failed')
            print(f'[Tweet] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            print(f'[Tweet] Result: Success')
            print(f'[Tweet] Tweet: https://twitter.com/i/status/{result_tweet["id"]}')

    # Twitter にダイレクトメッセージを送信
    if 'DirectMessage' in config.NOTIFY_TYPE:

        print('-' * terminal_columns)

        # ダイレクトメッセージを送信
        try:
            result_directmessage:dict = twitter.sendDirectMessage(message, image_path=image, destination=config.NOTIFY_DIRECTMESSAGE_TO)
        except Exception as error:
            print(f'[DirectMessage] Result: Failed')
            print(f'[DirectMessage] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            recipient_id = result_directmessage['event']['message_create']['target']['recipient_id']
            sender_id = result_directmessage['event']['message_create']['sender_id']
            print(f'[DirectMessage] Result: Success')
            print(f'[DirectMessage] Message: https://twitter.com/messages/{recipient_id}-{sender_id}')

    print('=' * terminal_columns)


if __name__ == '__main__':
    main()
