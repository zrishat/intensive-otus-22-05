"""
views
"""
# pylint: skip-file
# flake8: noqa
import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
import requests
from search_hotels.configuration_cities_hotels import cities_with_id
from search_hotels.forms import SearchHotelsForm
from travelru.settings import TOKEN_AVIASALES


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


def get_hotels_data(check_in: datetime.date, check_out: datetime.date, city_id: str, amount_guests: int) -> list[dict]:
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
    print('url', url, params)
    hotel_data = []
    for value_hotel_data in dirty_hotel_data['popularity']:
        try:
            one_hotel_info = {'name': value_hotel_data.get('name'),
                              'stars': value_hotel_data.get('stars'),
                              'hotel_type': value_hotel_data.get('hotel_type'),
                              'price': value_hotel_data.get('last_price_info')['price'],
                              'nights': value_hotel_data.get('last_price_info')['nights'],
                              'check_in': value_hotel_data.get('last_price_info')['search_params']['checkIn'],
                              'check_out': value_hotel_data.get('last_price_info')['search_params']['checkOut'],
                              'amount_guests': amount_guests}
            hotel_data.append(one_hotel_info)

        except TypeError:
            pass
    return hotel_data

def search_hotels(request):
    """
    search_hotels
    """
    # today_date = datetime.today().strftime("%Y-%m-%d")
    cities = cities_with_id
    if request.method == "POST":
        search_form = SearchHotelsForm(request.POST)
        if search_form.is_valid():
            city = search_form.cleaned_data['city']
            check_in = search_form.cleaned_data['check_in']
            check_out = search_form.cleaned_data['check_out']
            amount_guests = int(search_form.cleaned_data['amount_guests'])
            print(city, check_in, check_out)
            if check_out <= check_in:
                search_form.add_error('check_out', 'Дата выезда не может быть раньше даты въезда!')
                return render(request, "search_hotels.html", {'form': search_form})
            city_id = get_id_from_city(city, cities_with_id)
            if city_id == 'error':
                search_form.add_error('city', 'Такого города нет в базе')
                return render(request, "search_hotels.html", {'form': search_form})

            hotel_data = get_hotels_data(check_in, check_out, city_id, amount_guests)
            print('hotel data', hotel_data)

            return render(request, "search_hotels.html", {'form': search_form,
                                                          # 'today_date': today_date,
                                                          'hotel_data': hotel_data,
                                                          'cities': cities})  # pylint: disable=line-too-long
        else:  # pylint: disable=C0305
            return render(request, "search_hotels.html", {'form': search_form})
    else:
        search_form = SearchHotelsForm()

        return render(request, "search_hotels.html", {'form': search_form,
                                                      # 'today_date': today_date,
                                                      'cities': cities})
