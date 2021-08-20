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
    featured_apartments = Apartment.objects.filter(features_flag=1)
    context ={
        'main_menus': main_menus,
        'persons': persons,
        'apartments': apartments,
        'featured_apartments': featured_apartments,
    }
    return render(request, 'top/post_list.html', context)
