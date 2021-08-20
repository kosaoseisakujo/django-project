from django.shortcuts import render
from .models import Apartment

# Create your views here.
def apartment(request):
    apartments = Apartment.objects.all()
    context ={
        'apartments': apartments
    }
    return render(request, 'top/apartment.html', context)
