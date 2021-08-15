
from django.http import HttpRequest

def some_processor(request: HttpRequest):
    # 何かテンプレートコンテキストに追加するものを生成
    # dic = create_dict()
    # return dic
    return {
        'some_test_msg': '後から効いてくるスパイス'
    }
