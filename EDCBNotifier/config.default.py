
# ====================  環境設定  ====================

# [] で囲われている部分は配列 (list)
# {} で囲われている部分は辞書 (dict)
# 文字列は必ずシングルクオート ('') で囲んでください
# ハッシュ (#) をつけるとコメントになります (// はコメントにならない)
# 文字コード UTF-8 (BOM なし)・改行コード LF 以外で保存すると動作しなくなるので注意（メモ帳は基本的に NG）
# できれば VSCode などのシンタックスハイライトのあるエディタでの編集を推奨します


# 通知タイプ
# LINE (LINE Notify)・Tweet (ツイート)・DirectMessage (ダイレクトメッセージ) から設定
# [] 内にカンマ区切りで複数設定できます

# ex (LINE): NOTIFY_TYPE = ['LINE']
# ex (ツイート): NOTIFY_TYPE = ['Tweet']
# ex (ダイレクトメッセージ): NOTIFY_TYPE = ['DirectMessage']
# ex (LINE とツイート): NOTIFY_TYPE = ['LINE', 'Tweet']
# ex (LINE とダイレクトメッセージ): NOTIFY_TYPE = ['LINE', 'DirectMessage']
# ex (全て): NOTIFY_TYPE = ['LINE', 'Tweet', 'DirectMessage']

NOTIFY_TYPE = ['LINE', 'Tweet', 'DirectMessage']


# 通知を行うイベント
# 通知イベントのオン・オフを指定できます（たとえば頻度の多い PostNotify だけ通知しない設定も可能）
# ここで設定したイベントだけが通知されます（通知オフ） 設定されなかったイベントは通知されない（通知オフ）
# 各 .bat ファイルを配置しないことでも通知イベントのオン・オフは可能ですが、できるだけこの設定を使うことを推奨します

# PostAddReserve … 予約を追加したとき ( PostAddReserve.bat が実行されたとき)
# PostChgReserve … 予約を変更したとき ( PostChgReserve.bat が実行されたとき)
# PostRecStart … 録画を開始したとき（ PostRecStart.bat が実行されたとき）
# PostRecEnd … 録画を終了したとき（ PostRecEnd.bat が実行されたとき）
# PostNotify … 更新通知が送られたとき（ PostNotify.bat が実行されたとき）

# ex (全て通知): NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve', 'PostRecStart', 'PostRecEnd', 'PostNotify']
# ex (PostNotify 以外を通知): NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve', 'PostRecStart', 'PostRecEnd']
# ex (予約の追加・変更を通知): NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve']
# ex (録画の開始・終了を通知): NOTIFY_EVENT = ['PostRecStart', 'PostRecEnd']
# ex (録画結果だけ通知): NOTIFY_EVENT = ['PostRecEnd'] 

NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve', 'PostRecStart', 'PostRecEnd', 'PostNotify']


# 通知時に同時に送信する画像 (フルパスで指定)
# 画像を config.py と同じ階層に置く場合はファイル名だけの指定でも OK
# 画像サイズが大きすぎると送れない場合があるので注意
# None (シングルクオートはつけない) に設定した場合は画像を送信しません

# ex: NOTIFY_IMAGE = 'C:\Users\Test\Pictures\image.jpg'
# ex: NOTIFY_IMAGE = 'image.jpg'
# ex: NOTIFY_IMAGE = None

NOTIFY_IMAGE = None


# ダイレクトメッセージの宛先 (スクリーンネーム (@ から始まる ID) で指定)
# 上の設定で DirectMessage (ダイレクトメッセージ) を設定した場合に適用されます
# @ はつけずに指定してください 予め宛先のアカウントと DM が送信できる状態になっていないと送れません
# None (シングルクオートはつけない) に設定した場合は自分宛てに送信します

# ex: NOTIFY_DIRECTMESSAGE_TO = 'AbeShinzo'
# ex: NOTIFY_DIRECTMESSAGE_TO = None

NOTIFY_DIRECTMESSAGE_TO = None


# ログをファイルに保存（出力）するか
# True に設定した場合は、ログを config.py と同じフォルダの EDCBNotifier.log に保存します（コンソールに表示しない・前回のログは上書きされる）
# False に設定した場合は、ログを保存しません（コンソールに表示する）
# True・False にはシングルクオートをつけず、大文字で始めてください (true・false は NG)
# うまく通知されないときに True にしてログを確認してみるといいかも

NOTIFY_LOG = False


# ===================  メッセージ  ===================

# 改行を入れる場合は文字列内に \n と入力してください
# 文字列は + で連結できます
# 
# https://github.com/xtne6f/EDCB/blob/70b2331aadb328eb347fe0c4e4e23c8e91d286b7/Document/Readme_EpgTimer.txt#L929-L1008 と
# https://github.com/xtne6f/EDCB/blob/4c3bd5be3dc49607aa821d728105955c03fba4db/Document/Readme_Mod.txt#L451-L475 に記載されている EDCB のマクロが使えます
# マクロは $$ で囲んでください (ex: $ServiceName$)
# 
# また、独自にいくつかのマクロを追加しています
# ・$HashTag$ … 放送局名から取得したハッシュタグ (ハッシュタグは utils.py の get_hashtag() メソッドで定義) 
# ・$NotifyName$ … $NofityID$ から取得した更新通知タイプ（$NofityID$ = 1 … EPGデータ更新 2 … 予約情報更新 3 … 録画結果情報更新）
# ・$ServiceNameHankaku$ … $ServiceName$（放送局名）の英数字を半角に変換したもの
# ・$TitleHankaku$ … $Title$（番組タイトル）の英数字を半角に変換したもの
# ・$Title2Hankaku$ … $Title2$（番組タイトル・[]で囲まれている部分を削除したもの）の英数字を半角に変換したもの
# ・$TimeYYYY$ … 実行時刻の上2桁付き西暦年 (ex: 2020 (年))  $TimeYY$ … 実行時刻の上2桁なし西暦年 (ex: 20 (年))
# ・$TimeMM$ … 実行時刻の2桁固定の月 (ex: 07 (月))  $TimeM$ … 実行時刻の月 (ex: 7 (月))
# ・$TimeDD$ … 実行時刻の2桁固定の日 (ex: 09 (日))  $TimeD$ … 実行時刻の日 (ex: 9 (日))
# ・$TimeW$ … 実行時刻の曜日 (ex: 火 (曜日))
# ・$TimeHH$ … 実行時刻の2桁固定の時 (24時間) (ex: 06 (時))  $TimeH$ … 実行時刻の日 (ex: 6 (時))
# ・$TimeII$ … 実行時刻の2桁固定の分 (ex: 08 (分))  $TimeI$ … 実行時刻の分 (ex: 8 (分))
# ・$TimeSS$ … 実行時刻の2桁固定の秒 (ex: 02 (秒))  $TimeS$ … 実行時刻の分 (ex: 2 (秒))

NOTIFY_MESSAGE = {

    # 予約を追加したとき（ PostAddReserve.bat が実行されたとき）に送信するメッセージ
    'PostAddReserve': '➕ 予約追加: $SDYYYY$/$SDMM$/$SDDD$($SDW$) $ServiceNameHankaku$ $HashTag$ \n' +
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $TitleHankaku$',

    # 予約を変更したとき（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve': '📢 予約変更: $SDYYYY$/$SDMM$/$SDDD$($SDW$) $ServiceNameHankaku$ $HashTag$ \n' +
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $TitleHankaku$',

    # 録画を開始したとき（ PostRecStart.bat が実行されたとき）に送信するメッセージ
    'PostRecStart':   '⏺ 録画開始: $SDYYYY$/$SDMM$/$SDDD$($SDW$) $ServiceNameHankaku$ $HashTag$ \n' +
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $TitleHankaku$',

    # 録画を終了したとき（ PostRecEnd.bat が実行されたとき）に送信するメッセージ
    'PostRecEnd':     '⏹ 録画終了: $SDYYYY$/$SDMM$/$SDDD$($SDW$) $ServiceNameHankaku$ $HashTag$ \n' +
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $TitleHankaku$ \n' +
                      'Drop: $Drops$ Scramble: $Scrambles$ Comment: $Result$',

    # 更新通知が送られたとき（ PostNotify.bat が実行されたとき）に送信するメッセージ
    'PostNotify':     '🔔 通知: $NotifyName$ ($TimeMM$/$TimeDD$ $TimeHH$:$TimeII$:$TimeSS$)',

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
