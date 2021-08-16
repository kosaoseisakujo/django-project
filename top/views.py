from top.models import MainMenu, Person
from django.shortcuts import render

# Create your views here.
def post_list(request):
    # メインメニュー
    main_menus = MainMenu.objects.all()
    # Person
    persons = Person.objects.all()
    context ={
        'main_menus': main_menus,
        'persons': persons,
    }
    return render(request, 'top/post_list.html', context)

def news(request):
    context ={

    }
    return render(request, 'top/news.html', context)
