
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

## Usage

LINE Notify へ通知する場合は LINE Notify のアクセストークンが、Twitter へ通知する場合は Twitter API アプリが必須になります。  
LINE Notify のアクセストークンの作成には LINE へのログインが、Twitter API アプリの作成には Twitter の開発者アカウントがそれぞれ必要です。 

### 1. LINE Notify

LINE Notify へ通知しない場合は必要ありませんが、後述の Twitter の開発者アカウントを作成するよりも遥かに手順が簡単なので、やっておくことをおすすめします（さほど手間もかかりません）。

![Screenshot](https://user-images.githubusercontent.com/39271166/88357766-640c9480-cda7-11ea-9533-55d832b2284d.png)

[LINE Notify](https://notify-bot.line.me/ja/) にアクセスし、右上の［ログイン］から LINE へログインします（いつも使っているアカウントで構いません）。

![Screenshot](https://user-images.githubusercontent.com/39271166/88358109-a8e4fb00-cda8-11ea-8d11-a885bce9dc6a.png)

ログインできたら、右上のメニューから［マイページ］に移動します。

![Screenshot](https://user-images.githubusercontent.com/39271166/88369705-8ca68580-cdcb-11ea-82c8-f8eb363adfdf.png)

下の方にある「アクセストークンの発行(開発者向け)」へ行き、［トークンを発行する］をクリックします。

![Screenshot](https://user-images.githubusercontent.com/39271166/88370184-81a02500-cdcc-11ea-8147-772f3ceb9662.png)

トークン名は LINE Notify で通知が送られてきたときに \[EDCBNotifier\] のように付加される文字列です（ユニークである必要はないらしい）。  
通知を送信するトークルームは［1:1 でLINE Notifyから通知を受ける］か、任意のグループ LINE を選択してください。ここでは「1:1 でLINE Notifyから通知を受ける」を選択します。 

## License
[MIT Licence](LICENSE.txt)
