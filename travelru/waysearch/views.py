"""
views
"""
import requests
from datetime import datetime, timedelta
from django.shortcuts import render
from waysearch.configuration import IATA
from waysearch.models import City, Airport
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
    context = {"data": ""}
    #when Search button pulled down: make params for get request to aviasales, make context for render
    if request.method == "POST":
        url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'
        headers = {'Content-Type': 'application/json'}
        form_data = request.POST
        get_request_params = make_get_request_params(form_data)
        get_request_answer = requests.get(url, headers=headers, params=get_request_params).json()
        context = make_context_for_render(get_request_answer, get_request_params)
#        print(f"context = {context}")
    return render(request, 'search_avia.html', context)


def search_train_page(request):
    """
    search_train_page
    """
    return render(request, "search_train.html")

def make_get_request_params(form_data):
    """
    make request params from waysearch.form for makining get request to aviasales API
    """
    origin = form_data['departure_city']
    destination = form_data['arrival_city']
    departure_at = form_data['departure_date']
    return_at = form_data['arrival_date']
    # direct — получить рейсы без пересадок. По умолчанию false
    params = {'origin': from_city_to_code(origin),
#                  'destination': airport_name_to_IATAcode(destination),
              'destination': from_city_to_code(destination),
              'currency': 'rub',
              'departure_at': departure_at,
              'return_at': return_at,
              'sorting': 'price',
              'direct': 'true',
              'token': TOKEN_AVIASALES}
    return params

def make_context_for_render(get_request_answer, params):
    context = {}
    context['success'] = get_request_answer['success']
    context['currency_name_rus'] = "руб"
    context['get_request_params'] = params
    flights = get_request_answer['data']
    for flight in flights:
        flight['origin_name_rus'] = Airport.objects.get(code_IATA=flight['origin_airport']).city.name_rus
        flight['destination_name_rus'] = Airport.objects.get(code_IATA=flight['destination_airport']).city.name_rus
        flight['origin_airport_name_rus'] = Airport.objects.get(code_IATA=flight['origin_airport']).name_rus
        flight['destination_airport_name_rus'] = Airport.objects.get(code_IATA=flight['destination_airport']).name_rus
#        flight['departure_at_datetime'] = datetime.strptime(flight['departure_at'])

        departure_up_datetime_str = flight['departure_at'][:-3]+flight['departure_at'][-2:]
        departure_up_datetime = datetime.strptime(departure_up_datetime_str, '%Y-%m-%dT%H:%M:%S%z')
        flight['departure_up_date_str'] = departure_up_datetime.strftime("%d %B %Y")
        flight['departure_up_time_str'] = departure_up_datetime.strftime("%H:%M")
        depature_down_datetime = departure_up_datetime + timedelta(minutes=flight['duration'])
        flight['departure_down_date_str'] = depature_down_datetime.strftime("%d %B %Y")
        flight['departure_down_time_str'] = depature_down_datetime.strftime("%H:%M")
        # Если есть обратная дата, добаляем в словарь соответствующие поля
        if not params['return_at'] == '':
            return_up_datetime_str = flight['return_at'][:-3] + flight['return_at'][-2:]
            return_up_datetime = datetime.strptime(return_up_datetime_str, '%Y-%m-%dT%H:%M:%S%z')
            flight['return_up_date_str'] = return_up_datetime.strftime("%d %B %Y")
            flight['return_up_time_str'] = return_up_datetime.strftime("%H:%M")
            return_down_datetime = return_up_datetime + timedelta(minutes=flight['duration'])
            flight['return_down_date_str'] = return_down_datetime.strftime("%d %B %Y")
            flight['return_down_time_str'] = return_down_datetime.strftime("%H:%M")

    context['flights'] = flights
#    print(f"make_context_for_render: context = {context}")
    return context

def from_city_to_code(code):
    """
    from_city_to_code
    """
    data_cities = IATA
    for city in data_cities:
        if city['city'] == code:
            return city['iata']
    return ""

def airport_name_to_IATAcode(airport_name):
    """
    from_city_to_code
    """
    print(f"start airport_name_to_IATAcode, airport_name = {airport_name}")
    airport = Airport.objects.get(name_rus=airport_name)
    print(airport)
    if airport:
        print("return airport_name_to_IATAcode")
        return airport.code_IATA
    print("No such airport IATA code!")
    return ""