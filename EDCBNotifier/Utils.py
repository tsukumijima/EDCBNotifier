
import colorama
import datetime
import jaconv
import os
import sys

import config


class Utils:

    # EDCBNotifier のバージョン
    VERSION = 'v1.2.0'


    @staticmethod
    def getMacro(environ: os._Environ) -> dict:
        """
        環境変数に格納されているマクロを取得し、辞書にして返す
        environ には os.environ を渡す

        Args:
            environ (os._Environ): os.environ の値

        Returns:
            dict: マクロの値が入った辞書
        """

        # 実行時刻
        time = datetime.datetime.now()

        # 値が存在しなかった場合の初期値
        macro_default = '--'

        # マクロテーブル
        # 一部のみ利用できる、もしくは利用できないマクロも含む（注釈あり）
        macro_table = {

            # 標準マクロ
            'FilePath': environ.get('FilePath', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'FolderPath': environ.get('FolderPath', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'FileName': environ.get('FileName', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Title': environ.get('Title', macro_default),
            'Title2': environ.get('Title2', macro_default),
            'SDYYYY': environ.get('SDYYYY', macro_default),
            'SDYY': environ.get('SDYY', macro_default),
            'SDMM': environ.get('SDMM', macro_default),
            'SDM': environ.get('SDM', macro_default),
            'SDDD': environ.get('SDDD', macro_default),
            'SDD': environ.get('SDD', macro_default),
            'SDW': environ.get('SDW', macro_default),
            'STHH': environ.get('STHH', macro_default),
            'STH': environ.get('STH', macro_default),
            'STMM': environ.get('STMM', macro_default),
            'STM': environ.get('STM', macro_default),
            'STSS': environ.get('STSS', macro_default),
            'STS': environ.get('STS', macro_default),
            'EDYYYY': environ.get('EDYYYY', macro_default),
            'EDYY': environ.get('EDYY', macro_default),
            'EDMM': environ.get('EDMM', macro_default),
            'EDM': environ.get('EDM', macro_default),
            'EDDD': environ.get('EDDD', macro_default),
            'EDD': environ.get('EDD', macro_default),
            'EDW': environ.get('EDW', macro_default),
            'ETHH': environ.get('ETHH', macro_default),
            'ETH': environ.get('ETH', macro_default),
            'ETMM': environ.get('ETMM', macro_default),
            'ETM': environ.get('ETM', macro_default),
            'ETSS': environ.get('ETSS', macro_default),
            'ETS': environ.get('ETS', macro_default),
            'ONID10': environ.get('ONID10', macro_default),
            'TSID10': environ.get('TSID10', macro_default),
            'SID10': environ.get('SID10', macro_default),
            'EID10': environ.get('EID10', macro_default),
            'ONID16': environ.get('ONID16', macro_default),
            'TSID16': environ.get('TSID16', macro_default),
            'SID16': environ.get('SID16', macro_default),
            'EID16': environ.get('EID16', macro_default),
            'ServiceName': environ.get('ServiceName', macro_default),
            'SDYYYY28': environ.get('SDYYYY28', macro_default),
            'SDYY28': environ.get('SDYY28', macro_default),
            'SDMM28': environ.get('SDMM28', macro_default),
            'SDM28': environ.get('SDM28', macro_default),
            'SDDD28': environ.get('SDDD28', macro_default),
            'SDD28': environ.get('SDD28', macro_default),
            'SDW28': environ.get('SDW28', macro_default),
            'STHH28': environ.get('STHH28', macro_default),
            'STH28': environ.get('STH28', macro_default),
            'EDYYYY28': environ.get('EDYYYY28', macro_default),
            'EDYY28': environ.get('EDYY28', macro_default),
            'EDMM28': environ.get('EDMM28', macro_default),
            'EDM28': environ.get('EDM28', macro_default),
            'EDDD28': environ.get('EDDD28', macro_default),
            'EDD28': environ.get('EDD28', macro_default),
            'EDW28': environ.get('EDW28', macro_default),
            'ETHH28': environ.get('ETHH28', macro_default),
            'ETH28': environ.get('ETH28', macro_default),
            'DUHH': environ.get('DUHH', macro_default),
            'DUH': environ.get('DUH', macro_default),
            'DUMM': environ.get('DUMM', macro_default),
            'DUM': environ.get('DUM', macro_default),
            'DUSS': environ.get('DUSS', macro_default),
            'DUS': environ.get('DUS', macro_default),
            'Drops': environ.get('Drops', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Scrambles': environ.get('Scrambles', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Result': environ.get('Result', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'TitleF': environ.get('TitleF', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Title2F': environ.get('Title2F', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Genre': environ.get('Genre', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            'Genre2': environ.get('Genre2', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            'AddKey': environ.get('AddKey', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'SubTitle': environ.get('SubTitle', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            'SubTitle2': environ.get('SubTitle2', macro_default),  # 利用不可（RecName_Macro.dll のみ）

            # xtne6f 版で追加されたマクロ
            'BatFileTag': environ.get('BatFileTag', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ（？）
            'RecInfoID': environ.get('ReserveID', macro_default),  # PostRecEnd.bat のみ
            'ReserveID': environ.get('ReserveID', macro_default),  # PostRecEnd.bat 以外のみ
            'RecMode': environ.get('RecMode', macro_default),  # PostRecEnd.bat 以外のみ
            'ReserveComment': environ.get('ReserveComment', macro_default),  # PostRecEnd.bat 以外のみ
            'NotifyID': environ.get('NotifyID', macro_default),  # PostNotify.bat のみ

            # EDCBNotifier 独自マクロ
            'HashTag': Utils.getChannelHashtag(jaconv.z2h(environ.get('ServiceName', macro_default), digit=True, ascii=True, kana=False)),
            'HashTagTitle': Utils.getProgramHashtag(jaconv.z2h(environ.get('Title', macro_default), digit=True, ascii=True, kana=False)),
            'NotifyName': Utils.getNotifyType(int(environ.get('NotifyID', macro_default))),
            'ServiceNameHankaku': jaconv.z2h(environ.get('ServiceName', macro_default), digit=True, ascii=True, kana=False),
            'TitleHankaku': jaconv.z2h(environ.get('Title', macro_default), digit=True, ascii=True, kana=False),
            'Title2Hankaku': jaconv.z2h(environ.get('Title2', macro_default), digit=True, ascii=True, kana=False),
            'TimeYYYY': time.strftime('%Y'),
            'TimeYY': time.strftime('%y'),
            'TimeMM': time.strftime('%m'),
            'TimeM': str(int(time.strftime('%m'))),
            'TimeDD': time.strftime('%d'),
            'TimeD': str(int(time.strftime('%d'))),
            'TimeW': Utils.getExecutionDay(),
            'TimeHH': time.strftime('%H'),
            'TimeH': str(int(time.strftime('%H'))),
            'TimeII': time.strftime('%M'),
            'TimeI': str(int(time.strftime('%M'))),
            'TimeSS': time.strftime('%S'),
            'TimeS': str(int(time.strftime('%S'))),
        }

        return macro_table


    @staticmethod
    def getChannelHashtag(channel_name: str) -> str:
        """
        チャンネル名からハッシュタグを取得する
        BS-TBS が TBS と判定されるといったことがないように、BS・CS 局を先に判定する
        channel_name には半角に変換済みのチャンネル名が入るので注意
        ref: https://nyanshiba.com/blog/dtv-edcb-twitter

        Args:
            channel_name (str): チャンネル名

        Returns:
            str: チャンネル名に紐づくハッシュタグ
        """

        # BS・CS
        if 'NHKBS1' in channel_name:
            hashtag = '#nhkbs1'
        elif 'NHKBSプレミアム' in channel_name:
            hashtag = '#nhkbsp'
        elif 'BS日テレ' in channel_name:
            hashtag = '#bsntv'
        elif 'BS朝日' in channel_name:
            hashtag = '#bsasahi'
        elif 'BS-TBS' in channel_name:
            hashtag = '#bstbs'
        elif 'BSテレ東' in channel_name:
            hashtag = '#bstvtokyo'
        elif 'BSフジ' in channel_name:
            hashtag = '#bsfuji'
        elif 'BS11イレブン' in channel_name:
            hashtag = '#bs11'
        elif 'BS12トゥエルビ' in channel_name:
            hashtag = '#bs12'
        elif 'AT-X' in channel_name:
            hashtag = '#at_x'

        # 地デジ
        elif 'NHK総合' in channel_name:
            hashtag = '#nhk'
        elif 'NHKEテレ' in channel_name:
            hashtag = '#etv'
        elif 'tvk' in channel_name:
            hashtag = '#tvk'
        elif 'チバテレ' in channel_name:
            hashtag = '#chibatv'
        elif '日テレ' in channel_name:
            hashtag = '#ntv'
        elif 'テレビ朝日' in channel_name:
            hashtag = '#tvasahi'
        elif 'TBS' in channel_name:
            hashtag = '#tbs'
        elif 'テレビ東京' in channel_name:
            hashtag = '#tvtokyo'
        elif 'フジテレビ' in channel_name:
            hashtag = '#fujitv'
        elif 'TOKYO MX' in channel_name:
            hashtag = '#tokyomx'

        # ハッシュタグが見つからないのでそのまま利用
        else:
            hashtag = '#' + channel_name

        return hashtag


    @staticmethod
    def getProgramHashtag(program_title: str) -> str:
        """
        番組タイトルからハッシュタグを取得する
        program_title には半角に変換済みのタイトル名が入るので注意

        Args:
            title (str): 番組タイトル

        Returns:
            str: 番組タイトルに紐づくハッシュタグ
        """

        # dict 内に指定された番組タイトルが存在するか
        for hashtag_title in config.NOTIFY_HASHTAG_TITLE.keys():
            if hashtag_title in program_title:
                return config.NOTIFY_HASHTAG_TITLE[hashtag_title]

        # 存在しなかったら空文字列を返す
        return ''


    @staticmethod
    def getNotifyType(notify_id: int) -> str:
        """
        NotifyID から通知の種類を取得する

        Args:
            notify_id (int): EDCB の NotifyID

        Returns:
            str: 通知の種類
        """

        if notify_id == 1:
            notify_name = 'EPGデータ更新'
        elif notify_id == 2:
            notify_name = '予約情報更新'
        elif notify_id == 3:
            notify_name = '録画結果情報更新'
        else:
            notify_name = '更新なし'

        return notify_name


    @staticmethod
    def getExecutionTime() -> str:
        """
        EDCBNotifier の実行時刻をフォーマットして返す

        Returns:
            str: EDCBNotifier の実行時刻
        """
        return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')


    @staticmethod
    def getExecutionDay() -> str:
        """
        EDCBNotifier の実行日を返す
        ref: https://note.nkmk.me/python-datetime-day-locale-function/

        Returns:
            str: EDCBNotifier の実行日
        """
        weeklist = ['月', '火', '水', '木', '金', '土', '日']
        return weeklist[datetime.datetime.now().weekday()]


    @staticmethod
    def error(message: str) -> None:
        """
        エラーメッセージを表示して終了する

        Args:
            message (str): エラーメッセージ
        """
        print(colorama.Fore.RED + 'Error: ' + message, end='\n\n')
        sys.exit(1)
