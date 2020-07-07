
# ====================  環境設定  ====================

# 通知タイプ
# LINE・Twitter・ALL から設定
# ex: NOTIFY_TYPE = 'LINE'
# ex: NOTIFY_TYPE = 'Twitter'
# ex: NOTIFY_TYPE = 'ALL'

NOTIFY_TYPE = 'ALL'

# 通知時に同時に送信する画像
# フルパスで指定する
# config.py と同じ階層に置く場合はファイル名だけの指定でもOK
# None (シングルクオートはつけない) に設定した場合は通知を送信しない
# ex: NOTIFY_IMAGE = 'C:\Users\Test\Pictures\image.jpg'
# ex: NOTIFY_IMAGE = 'image.jpg'
# ex: NOTIFY_IMAGE = None

NOTIFY_IMAGE = None

# Twitter の通知方法
# Tweet (ツイート) または DirectMessage (ダイレクトメッセージ) を設定
# ex: NOTIFY_TWITTER_TYPE = 'Tweet'
# ex: NOTIFY_TWITTER_TYPE = 'DirectMessage'

NOTIFY_TWITTER_TYPE = 'Tweet'

# ダイレクトメッセージの宛先 (スクリーンネームで指定)
# 上の設定で DirectMessage (ダイレクトメッセージ) を指定した場合に利用される
# None (シングルクオートはつけない) に設定した場合は自分宛てに送信する
# ex: NOTIFY_TWITTER_DESTINATION = 'AbeShinzo'
# ex: NOTIFY_TWITTER_DESTINATION = None

NOTIFY_TWITTER_DESTINATION = None

# ===================  メッセージ  ===================

# 改行を入れる場合は文字列内に \n といれてください

NOTIFY_MESSAGE = {

    # 予約を追加したとき（ PostAddReserve.bat が実行されたとき）に送信するメッセージ
    'PostAddReserve': '予約を追加しました。',

    # 予約を変更したとき（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve': '予約を変更しました。',

    # 録画を開始したとき（ PostRecStart.bat が実行されたとき）に送信するメッセージ
    'PostRecStart': '録画を開始しました。',

    # 録画を終了したとき（ PostRecEnd.bat が実行されたとき）に送信するメッセージ
    'PostRecEnd': '録画を終了しました。',

    # 更新通知が送られたとき（ PostNotify.bat が実行されたとき）に送信するメッセージ
    'PostNotify': '更新を通知します。',

}

# ==================  LINE Notify  ==================

# LINE Notify のアクセストークン
LINE_ACCESS_TOKEN = 'YOUR_LINE_ACCESS_TOKEN'

# ==================  Twitter API  ==================

# Twitter API のコンシューマーキー
TWITTER_CONSUMER_KEY = 'YOUR_TWITTER_CONSUMER_KEY'

# Twitter API のコンシューマーシークレット
TWITTER_CONSUMER_SECRET = 'YOUR_TWITTER_CONSUMER_SECRET'

# Twitter API のアクセストークン
TWITTER_ACCESS_TOKEN = 'YOUR_TWITTER_ACCESS_TOKEN'

# Twitter API のアクセストークンシークレット
TWITTER_ACCESS_TOKEN_SECRET = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'
