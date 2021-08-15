
from django.http import HttpRequest

def some_processor(request: HttpRequest):
    # 何かテンプレートコンテキストに追加するものを生成
    # dic = create_dict()
    # return dic
    return {
        'IMAGE_PATH': 'https://cosaoyuji.s3.ap-northeast-1.amazonaws.com/images/',
        'IMAGE_PATH_TEST': 'https://cosaoyuji.s3.ap-northeast-1.amazonaws.com/',
        'TEST': 'TEST',
    }
