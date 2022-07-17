"""
views
"""
# flake8: noqa
import requests
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from waysearch.forms import WaysearchForm
from waysearch.configuration import IATA
from travelru.settings import TOKEN_AVIASALES
from my_travel.models import Item, Avia


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
        data = request.POST
        origin = data['departure_city']
        destination = data['arrival_city']

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

        departure_at = data['departure_date']
        return_at = data['arrival_date']
        if departure_at > return_at:
            search_avia.add_error('departure_date',
                                  'Дата возвращения должна быть позже даты вылета')
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
            data_info = requests.get(url, headers=headers, params=params).json()
        except Exception:  # pylint: disable=broad-except
            search_avia.add_error('departure_city', 'Сервис API недоступен.')
            return render(request, 'search_avia.html', {'form': search_avia})
        data_info['data_f'] = data
        print(data_info)
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
            if iata_tag['city_name'] == city:
                return iata_tag['code']
    return ""

def add_avia_to_travel(request):
    name = request.POST['name']
    print(request.POST)
    price = float(request.POST['price'].replace(",", "."))
    print(price)
    print(request.user)
    datetime_beg = datetime.strptime(request.POST['datetime_beg'], "%Y-%m-%dT%H:%M:%S%z")
    date_beg = datetime_beg.date()
    time_beg = datetime_beg.time()
    print(datetime_beg)
    datetime_end = datetime_beg + timedelta(minutes=int(request.POST['duration']))
    date_end = datetime_end.date()
    time_end = datetime_end.time()
    print(datetime_end)
    # time_beg = datetime.strptime("13:00", "%H:%M").time()
    # time_end = datetime.strptime("11:00", "%H:%M").time()
    #user = authenticate(username='guest', password='fdsa4321')

    if not request.user.is_authenticated:
        print('AnonimousUser detected!')
        user = authenticate(username='guest', password='fdsa4321')
    else:
        user = request.user
    item = Item.objects.create(name=name, item_type="AVIA", price=price, user=user,
                                date_beg=date_beg, date_end=date_end,
                                time_beg=time_beg, time_end=time_end)
    print(item)
    #    avia = Avia.objects.create(item=item, link="testlink")
#    hoteldata =
#    add_hotel_item_to_models(hotel_data)
#    return render(request, 'search_avia.html')
    return HttpResponseRedirect('/my-travel')
