"""
views
"""
# flake8: noqa
import requests
from django.shortcuts import render
from waysearch.forms import WaysearchForm
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
    search_avia = WaysearchForm()
    if request.method == "POST":
        search_avia = WaysearchForm(request.POST)
        url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'
        headers = {'Content-Type': 'application/json'}
        form_data = request.POST
        origin = form_data['departure_city']
        destination = form_data['arrival_city']

        city_1, city_2 = False, False
        for city_iata in IATA:
            if city_iata['city_name'].lower() in origin.lower():
                city_1 = True
            if city_iata['city_name'].lower() in destination.lower():
                city_2 = True
        if not city_1:
            search_avia.add_error('departure_city', f'Город откуда - {origin} не найден')
        if not city_2:
            search_avia.add_error('arrival_city', f'Город куда - {destination} не найден')
        if not city_1 or not city_2:
            return render(request, 'search_avia.html', {'form': search_avia})

        departure_at = form_data['departure_date']
        return_at = form_data['arrival_date']
        if departure_at > return_at:
            search_avia.add_error('departure_date', f'Дата возвращения должна быть позже даты вылета')
            return render(request, 'search_avia.html', {'form': search_avia})
        # direct — получить рейсы без пересадок. По умолчанию false
        params = {'origin': from_city_to_code(origin),
                  'destination': from_city_to_code(destination),
                  'currency': 'rub',
                  'departure_at': departure_at,
                  'return_at': return_at,
                  'sorting': 'price',
                  'direct': 'true',
                  'token': TOKEN_AVIASALES}
        try:
            get_answer = requests.get(url, headers=headers, params=params).json()
        except Exception:  # pylint: disable=broad-except
            search_avia.add_error('departure_city', 'Сервис API недоступен.')
            return render(request, 'search_avia.html', {'form': search_avia})
        data_info = extract_data_from_answer(get_answer)
        data_info['data_f'] = form_data
    data_info["iata"] = IATA
    return render(request, 'search_avia.html', {'form': search_avia, "data": data_info})


def search_train_page(request):
    """
    search_train_page
    """
    return render(request, "search_train.html")


def from_city_to_code(city):
    """
    from_city_to_code
    """
    for iata_tag in IATA:
        if 'москва' in city.lower():
            airport = city.split()[-1].strip("()")
            if iata_tag['name'] == airport:
                return iata_tag['code']
            else:
                return 'MOW'
        else:
            if iata_tag['city_name'] == city:
                return iata_tag['code']
    return ""

def extract_data_from_answer(answer):
    data_info = {}
    if answer['success']:
        data_info['success'] = True
        flights = answer['data']
        for flight in flights:
            for iata_tag in IATA:
                if iata_tag['code'] == flight['origin_airport']:
                    if iata_tag['city_name'] == "Москва":
                        flight['depature_city_text'] = f"Москва ({iata_tag['name']})"
                    else:
                        flight['depature_city_text'] = iata_tag['city_name']
                if iata_tag['code'] == flight['destination_airport']:
                    if iata_tag['city_name'] == "Москва":
                        flight['arrival_city_text'] = f"Москва ({iata_tag['name']})"
                    else:
                        flight['arrival_city_text'] = iata_tag['city_name']
        data_info['data'] = flights
        return data_info




