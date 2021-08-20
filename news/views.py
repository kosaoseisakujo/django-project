from django.shortcuts import render

# Create your views here.
def news(request):
    context ={

    }
    return render(request, 'top/news.html', context)
