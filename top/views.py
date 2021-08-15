from top.models import MainMenu
from django.shortcuts import render

# Create your views here.
def post_list(request):
    # メインメニュー
    main_menus = MainMenu.objects.all()
    context ={
        'main_menus': main_menus,
    }
    return render(request, 'top/post_list.html', context)
