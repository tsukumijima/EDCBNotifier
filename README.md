
# EDCBNotifier

EDCB から LINE や Twitter（ツイート・DM）に通知を送るツールです。

## About・Feature

xtne6f 版 EDCB のバッチファイル実行機能を使い、

- LINE (LINE Notify)
- Twitter (ツイート)
- Twitter (ダイレクトメッセージ)

に EDCB の通知を送信できる Python 製ツールです。

たとえば、EDCB で録画が開始されたときに LINE で録画開始を番組名を添えて通知したり、EPG 自動予約で追加された予約を通知で確認することができます。

LINE への通知は LINE Notify を使って送信します。  
LINE Notify はアプリケーションからの通知を指定したユーザーやグループで受信することができるサービスです。  
通知メッセージは LINE Notify の公式アカウントから受信できます（一度使ってみたほうが早いかも）。

Twitter への通知はツイートでの通知に加え、ダイレクトメッセージでの送信も可能です。  
ダイレクトメッセージは自分宛てに送ることも、DM を送信できる他のアカウントに送ることもできます。  
たとえば、録画通知用の Twitter アカウントを作ってメインアカウントと相互フォローになり、録画通知用のアカウントからメインアカウント宛てに通知を送ることもできます。

通知できるイベントは、

- 予約を追加したとき (PostAddReserve.bat が実行されたとき)
- 予約を変更したとき (PostChgReserve.bat が実行されたとき)
- 録画を開始したとき (PostRecStart.bat が実行されたとき)
- 録画を終了したとき (PostRecEnd.bat が実行されたとき)
- 更新通知が送られたとき (PostNotify.bat が実行されたとき)

の 5 つです。

それぞれのイベントは、個別に通知するかどうかを設定できます。  
更新通知が頻繁に送られてきてうるさい、といったときに［更新通知が送られたとき］のイベントだけ通知しないようにすることも可能です。

通知するメッセージは 5 つのイベントごとに自由に変更できます。  
設定ファイルは Python スクリプトなので、Python の知識があればメッセージをより高度にカスタマイズすることもできそうです。  
EDCB からのマクロに加えて、放送局名から取得したハッシュタグや更新通知タイプ、放送局名やタイトル名の英数字の半角変換など、独自のマクロも用意しています。

## Install

### 1. ダウンロード

![Screenshot](https://user-images.githubusercontent.com/39271166/88381578-a357d700-cde1-11ea-9f5a-12f559af093a.png)

［Code］メニュー内の［Download Zip］をクリックし、EDCBNotifier をダウンロードします。  
または、[こちら](https://github.com/tsukumijima/EDCBNotifier/archive/master.zip) のリンクからでもダウンロードできます。

### 2. Python のインストール

EDCBNotifier の実行には Python (Python3) が必要です 。動作確認は Python 3.7 系と Python 3.8 系で行っています。

すでに Python3 がインストールされている場合はスキップしても構いませんが、Python2 がインストールされている場合は別途 Python3 をインストールしてください。  
（Python2 と Python3 は半分別物で、このうち Python2 は 2020 年 1 月でサポートが終了しています）

![Screenshot](https://user-images.githubusercontent.com/39271166/88384104-c042d900-cde6-11ea-89f3-a1341b5d998e.png)

[非公式 Python ダウンロードリンク](https://pythonlinks.python.jp/ja/index.html) から、Python3 のインストーラーをダウンロードします。  
とくにこだわりがないのであれば、一番上にある Windows (64bit) 用 Python 3.8 の最新版 ( 2020 年 7 月現在の最新は 3.8.5 ) をダウンロードしてください。  

[Python 公式サイト](https://www.python.org/downloads/windows/) からもダウンロードできますが、わかりにくいので前述のサイトからダウンロードすることをおすすめします。  
もし OS が 32bit の方は Windows (32bit) 用をダウンロードしてください（ほとんどいないと思うけど…）。  
Windows10 では Microsoft Store からもインストールすることができますが、安定していない上にストアアプリの制限の影響で正常に動かないことがあるため、非推奨です。


## Usage

EDCBNotifier の設定は EDCBNotifier/config.py にて行います。  
LINE Notify へ通知する場合は LINE Notify のアクセストークンが、Twitter へ通知する場合は Twitter API アプリが必須になります。  
LINE Notify のアクセストークンの作成には LINE へのログインが、Twitter API アプリの作成には Twitter の開発者アカウントがそれぞれ必要です。 

### 1. 設定

### 2. LINE Notify

LINE Notify へ通知しない場合は必要ありませんが、後述の Twitter の開発者アカウントを作成するよりも遥かに手順が簡単なので、やっておくことをおすすめします（さほど手間もかかりません）。

![Screenshot](https://user-images.githubusercontent.com/39271166/88371964-03de1880-cdd0-11ea-9768-e582d669e6f7.png)

[LINE Notify](https://notify-bot.line.me/ja/) にアクセスし、右上の［ログイン］から LINE へログインします（いつも使っているアカウントで構いません）。

![Screenshot](https://user-images.githubusercontent.com/39271166/88371966-0476af00-cdd0-11ea-85a9-9162a23f49ef.png)

ログインできたら、右上のメニューから［マイページ］に移動します。

![Screenshot](https://user-images.githubusercontent.com/39271166/88371969-06407280-cdd0-11ea-9e70-ed5b796d79e0.png)

下の方にある「アクセストークンの発行(開発者向け)」へ行き、［トークンを発行する］をクリックします。

![Screenshot](https://user-images.githubusercontent.com/39271166/88370184-81a02500-cdcc-11ea-8147-772f3ceb9662.png)

トークン名は LINE Notify で通知が送られてきたときに \[EDCBNotifier\] のように付加される文字列です（ユニークである必要はないらしい）。  
通知を送信するトークルームは［1:1 でLINE Notifyから通知を受ける］か、任意のグループ LINE を選択してください。  
ここでは「1:1 でLINE Notifyから通知を受ける」（現在ログインしているアカウントに届く）を選択します。 

![Screenshot](https://user-images.githubusercontent.com/39271166/88371432-fbd1a900-cdce-11ea-8e9f-2067360c32b9.png)

［発行する］をクリックするとアクセストークンが発行されるので、［コピー］をクリックしてクリップボードにコピーします。  
アクセストークンはこの画面を閉じると二度と表示されない（一度解除し同じ内容でもう一度発行することはできるがアクセストークンは変わる）ので、どこかにメモしておくと良いでしょう。

![Screenshot](https://user-images.githubusercontent.com/39271166/88371444-fecc9980-cdce-11ea-8293-b9a8bf765422.png)

画面を閉じると LINE Notify と設定したトークルームが連携されているはずです。

## License
[MIT Licence](LICENSE.txt)
