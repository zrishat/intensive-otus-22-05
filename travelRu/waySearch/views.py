import requests
from django.shortcuts import render

from travelRu.settings import TOKEN_AVIASALES


def index(request):
    return render(request, "index.html")


def search_avia_page(request):
    data_info = {"data": ""}
    if request.method == "POST":
        url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'
        headers = {'Content-Type': 'application/json'}
        data = request.POST
        origin = data['departure_city']
        destination = data['arrival_city']
        departure_at = data['departure_date']
        return_at = data['arrival_date']
        # direct — получить рейсы без пересадок. По умолчанию false
        params = {'origin': from_city_to_code(origin), 'destination': from_city_to_code(destination), 'currency': 'rub',
                  'departure_at': departure_at,
                  'return_at': return_at, 'sorting': 'price', 'direct': 'true', 'token': TOKEN_AVIASALES}
        # params = {'origin': 'MOW', 'destination': 'LED', 'currency': 'rub', 'departure_at': '2022-06-10',
        #           'sorting': 'price', 'direct': 'true', 'token': TOKEN_AVIASALES}
        data_info = requests.get(url, headers=headers, params=params).json()
    return render(request, 'search_avia.html', data_info)


def search_train_page(request):
    return render(request, "search_train.html")


def from_city_to_code(code):
    return code