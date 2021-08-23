from top.models import Menu, Person
from apartment.models import  Apartment
from news.models import Notice
from django.shortcuts import render

# Create your views here.
def post_list(request):
    # メインメニュー
    main_menus = Menu.objects.filter(main_flag=1)
    # Person
    persons = Person.objects.all()
    # アパート情報
    apartments = Apartment.objects.all()
    featured_apartments = Apartment.objects.filter(features_flag=1)
    main_apartment = Apartment.objects.get(main_flag=1)
    print(main_apartment)
    # ニュース&イベント
    notices = Notice.objects.all()[:3]
    context ={
        'main_menus': main_menus,
        'persons': persons,
        'apartments': apartments,
        'featured_apartments': featured_apartments,
        'notices': notices,
        'main_apartment': main_apartment
    }
    return render(request, 'top/post_list.html', context)
