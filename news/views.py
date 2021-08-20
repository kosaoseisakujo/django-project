from django.shortcuts import render
from .models import Notice

# Create your views here.
def news(request):
    notices = Notice.objects.all()
    context ={
        'notices': notices
    }
    return render(request, 'top/news.html', context)
