from top.models import MainMenu, Person
from apartment.models import  Apartment
from django.shortcuts import render

# Create your views here.
def post_list(request):
    # メインメニュー
    main_menus = MainMenu.objects.all()
    # Person
    persons = Person.objects.all()
    # アパート情報
    apartments = Apartment.objects.all()

    context ={
        'main_menus': main_menus,
        'persons': persons,
        'apartments': apartments,
    }
    return render(request, 'top/post_list.html', context)
