"""
views
"""
# pylint: skip-file
# flake8: noqa

from datetime import datetime
from typing import List

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
import requests
from search_hotels.configuration_cities_hotels import cities_with_id
from search_hotels.forms import SearchHotelsForm
from travelru.settings import TOKEN_AVIASALES
from my_travel.models import Item, Hotel


def get_id_from_city(city_name: str, cities_list: list):  # pylint: disable=E1136 # noqa: E501
    """
    get_id_from_city
    """
    for city in cities_list:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return 'error'


"""
запрос с формой
"""


def get_hotels_data(check_in: datetime.date, check_out: datetime.date, city_id: str, amount_guests: int) -> List[dict]:
    url = 'http://yasen.hotellook.com/tp/public/widget_location_dump.json'
    params = {'check_in': check_in,
              'check_out': check_out,
              'currency': 'rub',
              'language': 'ru',
              # 'limit': '5',
              'type': 'popularity',
              'id': city_id,
              'token': TOKEN_AVIASALES}

    dirty_hotel_data = requests.get(url, params=params).json()
    # print('url', url, params)
    hotel_data = []
    for value_hotel_data in dirty_hotel_data['popularity']:
        try:
            one_hotel_info = dict(name=value_hotel_data.get('name'), stars=value_hotel_data.get('stars'),
                                  hotel_type=value_hotel_data.get('hotel_type'),
                                  price=round(value_hotel_data.get('last_price_info')['price_pn']),
                                  nights=value_hotel_data.get('last_price_info')['nights'],
                                  check_in=datetime.strptime(
                                    value_hotel_data.get('last_price_info')['search_params']['checkIn'],
                                    '%Y-%m-%d').date(),
                                  check_out=datetime.strptime(
                                    value_hotel_data.get('last_price_info')['search_params']['checkOut'],
                                    '%Y-%m-%d').date(),
                                  amount_guests=amount_guests)
            hotel_data.append(one_hotel_info)

        except TypeError:
            pass

    return hotel_data


def get_sorted_hotels(hotels_list: List[dict]) -> List[dict]:
    sorted_hotels_list = sorted(hotels_list, key=lambda k: k['price'])
    return sorted_hotels_list


def search_hotels(request):
    """
    search_hotels
    """
    print('search_hotels')

    # today_date = datetime.today().strftime("%Y-%m-%d")
    cities = cities_with_id
    if request.method == "POST":
        print(request.POST)
        search_form = SearchHotelsForm(request.POST)
        if search_form.is_valid():
            city = search_form.cleaned_data['city']
            check_in = search_form.cleaned_data['check_in']
            check_out = search_form.cleaned_data['check_out']
            amount_guests = int(search_form.cleaned_data['amount_guests'])
            if check_out < check_in:
                search_form.add_error('check_out', 'Дата выезда не может быть раньше даты въезда!')
                return render(request, "search_hotels.html", {'form': search_form})
            elif check_out == check_in:
                search_form.add_error('check_out', 'Дата выезда не может совпадать с датой заезда!')
                return render(request, "search_hotels.html", {'form': search_form})
            city_id = get_id_from_city(city, cities_with_id)
            if city_id == 'error':
                search_form.add_error('city', 'Такого города нет в базе')
                return render(request, "search_hotels.html", {'form': search_form})

            hotel_data = get_hotels_data(check_in, check_out, city_id, amount_guests)
            sorted_hotel_data = get_sorted_hotels(hotel_data)
            # print('hotel data', hotel_data)
            # print('hotel data', sorted_hotel_data)
            return render(request, "search_hotels.html", {'form': search_form,
                                                          # 'today_date': today_date,
                                                          'after_request': True,
                                                          'hotel_data': sorted_hotel_data,
                                                          'cities': cities})  # pylint: disable=line-too-long
        else:  # pylint: disable=C0305
            return render(request, "search_hotels.html", {'form': search_form})
    else:
        search_form = SearchHotelsForm()

        return render(request, "search_hotels.html", {'form': search_form,
                                                      # 'today_date': today_date,
                                                      'cities': cities})


def add_hotel_to_travel(request):
    # print(request.POST)
    name = request.POST['name']
    # price = float(request.POST['price'].replace(",", "."))
    price = int(request.POST['price'])
    hotel_city = request.POST['city']
    date_beg = datetime.strptime(request.POST['check_in'], "%d-%m-%Y").date()
    date_end = datetime.strptime(request.POST['check_out'], "%d-%m-%Y").date()
    time_beg = datetime.strptime("13:00", "%H:%M").time()
    time_end = datetime.strptime("11:00", "%H:%M").time()

    if not request.user.is_authenticated:
        print('AnonimousUser detected!')
        user = authenticate(username='guest', password='fdsa4321')
    else:
        user = request.user

    item = Item.objects.create(name=name, item_type="HOTEL", price=price, user=user,
                               hotel_city=hotel_city,
                               date_beg=date_beg, date_end=date_end,
                               time_beg=time_beg, time_end=time_end)
#    add_hotel_item_to_models(hotel_data)
    return HttpResponseRedirect('/my-travel')
