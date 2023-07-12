import os
import mastodon


class Mastodon:
    """
    Mastodon でメッセージを送信する
    """

    def __init__(self, base_url: str, access_token: str):
        """
        Args:
            access_token (str): Mastodon のアクセストークン
        """

        # 初期化
        self.mastodon = mastodon.Mastodon(
            api_base_url=base_url,
            access_token=access_token
        )

        # 自分の情報を取得
        self.account_info = self.mastodon.me()

    def sendToot(self, message: str, image_path: str = None) -> dict:
        """
        トゥートを送信する

        Args:
            message (str): 送信するツイートの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: API レスポンスのデータ
        """

        if (image_path is not None and os.path.isfile(image_path)):

            # 画像をアップロードして media_id を取得
            media_id = self.mastodon.media_post(
                media_file=image_path,
                mine_type="image/jpeg"
            )['id']

            # 画像とテキストを送信
            response = self.mastodon.status_post(
                status=message,
                visibility='unlisted',
                media_ids=[media_id]
            )

        else:

            # テキストのみ送信
            response = self.mastodon.status_post(
                status=message,
                visibility='unlisted'
            )

        # API レスポンスを返す
        return response

    def sendDirectMessage(self, message: str, destination: str = None, image_path: str = None) -> dict:
        """
        ダイレクトメッセージを送信する

        Args:
            message (str): 送信するダイレクトメッセージの本文
            destination (str, optional): ダイレクトメッセージを送信するアカウントのスクリーンネーム. Defaults to None.
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: API レスポンスのデータ
        """

        if (image_path is not None and os.path.isfile(image_path)):

            # 画像をアップロードして media_id を取得
            media_id = self.mastodon.media_post(
                media_file=image_path,
                mine_type="image/jpeg"
            )['id']

            # 画像とテキストを送信
            response = self.mastodon.status_post(
                status=destination + " " + message,
                visibility='private',
                media_ids=[media_id]
            )

        else:

            # テキストのみ送信
            response = self.mastodon.status_post(
                status=destination + " " + message,
                visibility='private'
            )

        # API レスポンスを返す
        return response
