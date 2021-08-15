from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムタグとして登録する
@register.simple_tag
def link_tag(url):
    return url
