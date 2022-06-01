import json

import requests
from django.shortcuts import render
from data_info import token_name

# Create your views here.


def index(request):
    return render(request, "index.html")


def search_avia_page(request):
    return render(request, "search_avia.html")


def search_avia_tickets(request):
    url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'
    headers = {'Content-Type': 'application/json'}
    params = {'origin': 'MOW', 'destination': 'LED', 'currency': 'rub', 'departure_at': '2022-06-10',
              'sorting': 'price', 'direct': 'true', 'token': token_name}
    json_to_download = requests.get(url, headers=headers, params=params).json()

    print(f'link_got: {json_to_download}')

    return render(request, 'search_aviatickets.html', context=json_to_download)


def search_train_page(request):
    return render(request, "search_train.html")
