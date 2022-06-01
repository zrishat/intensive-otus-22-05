import requests
from django.shortcuts import render

from travelRu.settings import TOKEN_AVIASALES


def index(request):
    return render(request, "index.html")


def search_avia_page(request):
    if request.method == "POST":
        data = request.POST.items()
    print(dict(data))
    print(request.POST)
    return render(request, 'search_avia.html', {'data': data})
    # return render(request, "search_avia.html")


def search_avia_tickets(request):
    if request.method == "POST":
        print('POST')
    else:
        print('Another')
    data = request.POST.items()
    print(data)
    return render(request, 'search_avia.html', {'data': data})

    # url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'
    # headers = {'Content-Type': 'application/json'}
    # params = {'origin': 'MOW', 'destination': 'LED', 'currency': 'rub', 'departure_at': '2022-06-10',
    #           'sorting': 'price', 'direct': 'true', 'token': TOKEN_AVIASALES}
    # json_to_download = requests.get(url, headers=headers, params=params).json()
    #
    # print(f'link_got: {json_to_download}')
    #
    # return render(request, 'search_aviatickets.html', context=json_to_download)


def search_train_page(request):
    return render(request, "search_train.html")
