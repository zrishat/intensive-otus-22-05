from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'waySearch/index.html')


def search_avia_page(request):
    return render(request, 'waySearch/search_avia.html')


def search_train_page(request):
    return render(request, 'waySearch/search_train.html')