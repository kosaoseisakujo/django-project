
from django.http import HttpRequest
from top.models import Menu

def some_processor(request: HttpRequest):
    # 何かテンプレートコンテキストに追加するものを生成
    # dic = create_dict()
    # return dic
    GLOBAL_MENU = Menu.objects.filter(main_flag=1)
    return {
        'IMAGE_PATH': 'https://cosaoyuji.s3.ap-northeast-1.amazonaws.com/images/',
        'IMAGE_PATH_TEST': 'https://cosaoyuji.s3.ap-northeast-1.amazonaws.com/',
        'TEST': 'TEST',
        'GLOBAL_MENU': GLOBAL_MENU
    }
