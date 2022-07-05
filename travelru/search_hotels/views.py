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


def search_hotels(request):
    today_date = datetime.today().strftime("%Y-%m-%d")
    # today_date = datetime.today()

    """
    search_hotels
    """
    # data_info = {"popularity": ""}
    if request.method == "POST":
        url = 'http://yasen.hotellook.com/tp/public/widget_location_dump.json'
        # url = 'http://92.119.90.43:1992'
        headers = {'Content-Type': 'application/json'}
        search_form = SearchHotelsForm(request.POST)
        if search_form.is_valid():
            city = search_form.cleaned_data['city']
            check_in = search_form.cleaned_data['check_in']
            check_out = search_form.cleaned_data['check_out']
            amount_guests = search_form.cleaned_data['amount_guests']
            print(city, check_in, check_out)
            if check_out <= check_in:
                search_form.add_error('check_out', 'Дата выезда не может быть раньше даты въезда!')
                return render(request, "search_hotels.html", {'form': search_form})
            city_id = get_id_from_city(city, cities_with_id)
            if city_id == 'error':
                search_form.add_error('city', 'Такого города нет в базе')
                return render(request, "search_hotels.html", {'form': search_form})

            params = {'check_in': check_in,
                      'check_out': check_out,
                      'currency': 'rub',
                      'language': 'ru',
                      # 'limit': '5',
                      'type': 'popularity',
                      'id': city_id,
                      'token': TOKEN_AVIASALES}

            dirty_hotel_data = requests.get(url, headers=headers, params=params).json()
            print('url', url, headers, params)
            hotel_data = []
            for value_hotel_data in dirty_hotel_data['popularity']:
                try:
                    one_hotel_info = {'name': value_hotel_data['name'], 'stars': value_hotel_data['stars'],
                                      'hotel_type': value_hotel_data['hotel_type'],
                                      'price': value_hotel_data['last_price_info']['price'],
                                      'nights': value_hotel_data['last_price_info']['nights'],
                                      'check_in': value_hotel_data['last_price_info']['search_params']['checkIn'],
                                      'check_out': value_hotel_data['last_price_info']['search_params']['checkOut'],
                                      'amount_guests': int(amount_guests)}
                    hotel_data.append(one_hotel_info)

                except TypeError:
                    pass

            print('hotel data', hotel_data)

            return render(request, "search_hotels.html", {'form': search_form,
                                                          'today_date': today_date,
                                                          'hotel_data': hotel_data})  # pylint: disable=line-too-long
        else:  # pylint: disable=C0305
            return render(request, "search_hotels.html", {'form': search_form})
    else:
        search_form = SearchHotelsForm()
        cities = cities_with_id
        return render(request, "search_hotels.html", {'form': search_form, 'today_date': today_date, 'cities': cities})
