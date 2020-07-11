
# Utils


# 環境変数に格納されているマクロを取得してdictで返す
# environ には os.environ を渡す
def get_macro(environ):

    # 値が存在しなかった場合の初期値
    macro_default = '--'

    # マクロテーブル
    macro_table = {

        'FilePath': environ.get('FilePath', macro_default),
        'FolderPath': environ.get('FolderPath', macro_default),
        'FileName': environ.get('FileName', macro_default),
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
        'Drops': environ.get('Drops', macro_default),
        'Scrambles': environ.get('Scrambles', macro_default),
        'Result': environ.get('Result', macro_default),
        'TitleF': environ.get('TitleF', macro_default),
        'Title2F': environ.get('Title2F', macro_default),
        'Genre': environ.get('Genre', macro_default),
        'Genre2': environ.get('Genre2', macro_default),
        'AddKey': environ.get('AddKey', macro_default),
        'SubTitle': environ.get('SubTitle', macro_default),
        'SubTitle2': environ.get('SubTitle2', macro_default),
        
        'ReserveID': environ.get('ReserveID', macro_default),
        'RecMode': environ.get('RecMode', macro_default),
        'ReserveComment': environ.get('ReserveComment', macro_default),
        'NotifyID': environ.get('NotifyID', macro_default),
        
        'HashTag': get_hashtag(environ.get('ServiceName', macro_default)),
        'NotifyName': get_notify_name(environ.get('NotifyID', macro_default)),

    }

    return macro_table


# 放送局名からハッシュタグを取得する
# BS-TBS が TBS と判定されるといったことがないよう BS 局を先に判定する
# 参考: https://nyanshiba.com/blog/dtv-edcb-twitter
def get_hashtag(service_name):

    # BS

    if 'ＮＨＫＢＳ１' in service_name:

        hashtag = '#nhkbs1'

    elif 'ＮＨＫＢＳプレミアム' in service_name:

        hashtag = '#nhkbsp'

    elif 'ＢＳ日テレ' in service_name:

        hashtag = '#bsntv'

    elif 'ＢＳ朝日' in service_name:

        hashtag = '#bsasahi'

    elif 'ＢＳ－ＴＢＳ' in service_name:

        hashtag = '#bstbs'

    elif 'ＢＳテレ東' in service_name:

        hashtag = '#bstvtokyo'

    elif 'ＢＳフジ' in service_name:

        hashtag = '#bsfuji'

    elif 'ＢＳ１１イレブン' in service_name:

        hashtag = '#bs11'

    elif 'ＢＳ１２トゥエルビ' in service_name:

        hashtag = '#bs12'

    # 地デジ
    
    elif 'ＮＨＫ総合' in service_name:

        hashtag = '#nhk'

    elif 'ＮＨＫＥテレ' in service_name:

        hashtag = '#etv'

    elif 'ｔｖｋ' in service_name:

        hashtag = '#tvk'

    elif 'チバテレ' in service_name:

        hashtag = '#chibatv'

    elif '日テレ' in service_name:

        hashtag = '#ntv'

    elif 'テレビ朝日' in service_name:

        hashtag = '#tvasahi'

    elif 'ＴＢＳ' in service_name:

        hashtag = '#tbs'

    elif 'テレビ東京' in service_name:

        hashtag = '#tvtokyo'

    elif 'フジテレビ' in service_name:

        hashtag = '#fujitv'

    elif 'ＴＯＫＹＯ　ＭＸ' in service_name:

        hashtag = '#tokyomx'

    else:

        # ハッシュタグが見つからないのでそのまま利用
        hashtag = '#' + service_name

    return hashtag


# NotifyID から NotifyName を取得する
def get_notify_name(notify_id):

    if notify_id == '1':

        notify_name = 'EPGデータ更新'

    elif notify_id == '2':

        notify_name = '予約情報更新'

    elif notify_id == '3':

        notify_name = '録画結果情報更新'

    else:

        notify_name = '更新なし'

    return notify_name
    

# バージョン情報
def get_version():

    return '1.0.0'
