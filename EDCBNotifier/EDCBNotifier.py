
import colorama
import os
import ruamel.yaml
import shutil
import sys

from SendDiscord import Discord
from SendLINE import LINE
from SendTwitter import Twitter

# バージョン情報
VERSION = '1.2.0'

# ベースディレクトリ
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

# ターミナルの横幅
# conhost.exe だと -1px しないと改行されてしまう
TERMINAL_WIDTH = shutil.get_terminal_size().columns - 1

# 環境設定を読み込む
CONFIG_YAML = BASE_DIR + '/EDCBNotifier.yaml'
if os.path.exists(CONFIG_YAML) is False:
    print('=' * TERMINAL_WIDTH)
    print('Error: EDCBNotifier.yaml does not exist.')
    print('       Copy it from EDCBNotifier.example.yaml and edit it to suit your environment.')
    print('=' * TERMINAL_WIDTH)
    sys.exit(1)
with open(CONFIG_YAML, encoding='utf-8') as stream:
    CONFIG = ruamel.yaml.YAML().load(stream)


def main():

    # 初期化
    from Utils import Utils  # 循環インポートの防止
    colorama.init(autoreset=True)

    # 標準出力をファイルに変更
    if CONFIG['general']['logging']:
        sys.stdout = open(BASE_DIR + '/EDCBNotifier.log', mode='w', encoding='utf-8')
        sys.stderr = open(BASE_DIR + '/EDCBNotifier.log', mode='w', encoding='utf-8')

    # ヘッダー
    print('=' * TERMINAL_WIDTH)
    print(f'+++++{f"EDCBNotifier version {VERSION}":^{TERMINAL_WIDTH - 10}}+++++')
    print('=' * TERMINAL_WIDTH)

    # 引数を受け取る
    if len(sys.argv) > 1:

        # 呼び出し元のイベント
        caller = sys.argv[1]  # 呼び出し元のバッチファイルの名前
        print(f'Event: {caller}')

        # 実行時刻
        print(f'Execution Time: {Utils.getExecutionTime()}')

        # NOTIFY_MESSAGE にあるイベントでかつ通知がオンになっていればメッセージをセット
        if (caller in CONFIG['message'] and caller in CONFIG['general']['notify_event']):
            # 配列になっているので、改行で連結する
            message = '\n'.join(CONFIG['message'][caller])

        # NOTIFY_MESSAGE にあるイベントだが、通知がオフになっているので終了
        elif caller in CONFIG['message']:
            print(f'Info: {caller} notification is off, so it ends.')
            print('=' * TERMINAL_WIDTH)
            sys.exit(0)

        # 引数が不正なので終了
        else:
            Utils.error('Invalid argument.')

    # 引数がないので終了
    else:
        Utils.error('Argument does not exist.')

    print('-' * TERMINAL_WIDTH)

    # マクロを取得
    macros = Utils.getMacro(os.environ)
    # メッセージを置換
    for macro, macro_value in macros.items():
        # $$ で囲われた文字を置換する
        message = message.replace(f'${macro}$', macro_value)

    print('Message: ' + message.replace('\n', '\n         '))

    # 送信する画像
    # パスをそのまま利用
    if (CONFIG['general']['notify_image'] is not None) and (os.path.isfile(CONFIG['general']['notify_image'])):
        image = CONFIG['general']['notify_image']

    # パスを取得して連結
    elif (CONFIG['general']['notify_image'] is not None) and (os.path.isfile(BASE_DIR + '/' + CONFIG['general']['notify_image'])):
        image = BASE_DIR + '/' + CONFIG['general']['notify_image']

    # 画像なし
    else:
        image = None

    # LINE Notify にメッセージを送信
    if 'LINE' in CONFIG['general']['notify_type']:

        print('-' * TERMINAL_WIDTH)

        line = LINE(CONFIG['line']['access_token'])

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
    if 'Discord' in CONFIG['general']['notify_type']:

        print('-' * TERMINAL_WIDTH)

        discord = Discord(CONFIG['discord']['webhook_url'])

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
    if 'Tweet' in CONFIG['general']['notify_type'] or 'DirectMessage' in CONFIG['general']['notify_type']:

        twitter = Twitter(
            CONFIG['twitter']['consumer_key'],
            CONFIG['twitter']['consumer_secret'],
            CONFIG['twitter']['access_token'],
            CONFIG['twitter']['access_token_secret'],
        )

    # Twitter にツイートを送信
    if 'Tweet' in CONFIG['general']['notify_type']:

        print('-' * TERMINAL_WIDTH)

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
    if 'DirectMessage' in CONFIG['general']['notify_type']:

        print('-' * TERMINAL_WIDTH)

        # ダイレクトメッセージを送信
        try:
            direct_message_destination = CONFIG['twitter']['direct_message_destination']
            result_directmessage:dict = twitter.sendDirectMessage(message, image_path=image, destination=direct_message_destination)
        except Exception as error:
            print(f'[DirectMessage] Result: Failed')
            print(f'[DirectMessage] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            recipient_id = result_directmessage['event']['message_create']['target']['recipient_id']
            sender_id = result_directmessage['event']['message_create']['sender_id']
            print(f'[DirectMessage] Result: Success')
            print(f'[DirectMessage] Message: https://twitter.com/messages/{recipient_id}-{sender_id}')

    print('=' * TERMINAL_WIDTH)


if __name__ == '__main__':
    main()
