"""
views
"""
import requests
from django.shortcuts import render
from waysearch.configuration import IATA
from travelru.settings import TOKEN_AVIASALES


def index(request):
    """
    index
    """
    return render(request, "index.html")


def search_avia_page(request):
    """
    search_avia_page
    """
    data_info = {"data": ""}
    if request.method == "POST":
        url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'
        headers = {'Content-Type': 'application/json'}
        data = request.POST
        # print(data)
        origin = data['departure_city']
        destination = data['arrival_city']
        departure_at = data['departure_date']
        return_at = data['arrival_date']
        # direct — получить рейсы без пересадок. По умолчанию false
        params = {'origin': from_city_to_code(origin),
                  'destination': from_city_to_code(destination),
                  'currency': 'rub',
                  'departure_at': departure_at,
                  'return_at': return_at,
                  'sorting': 'price',
                  'direct': 'true',
                  'token': TOKEN_AVIASALES}
        data_info = requests.get(url, headers=headers, params=params).json()
        print(data_info)
    return render(request, 'search_avia.html', data_info)


def search_train_page(request):
    """
    search_train_page
    """
    return render(request, "search_train.html")


def from_city_to_code(code):
    """
    from_city_to_code
    """
    data_cities = IATA
    for city in data_cities:
        if city['city'] == code:
            return city['iata']
    return ""
