"""
views
"""
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.


# def index(request):
#     return render(request, "search_hotels.html")
from search_hotels.configuration_cities_hotels import cities_with_id
from search_hotels.forms import SearchHotelsForm
from travelru.settings import TOKEN_AVIASALES


def get_id_from_city(city_name: str, cities_list: list[dict]):  # pylint: disable=E1136 # noqa: E501
    """
    get_id_from_city
    """
    for city in cities_list:
        if city['name'].lower() == city_name.lower():
            return city['id']
    raise BaseException


"""
запрос без формы
"""

# def search_hotels(request):
#     """
#     search_hotels
#     """
#     data_info = {"popularity": ""}
#     if request.method == "POST":
#         url = 'http://yasen.hotellook.com/tp/public/widget_location_dump.json'
#         headers = {'Content-Type': 'application/json'}
#         data = request.POST
#         print(data)
#         check_in = data['check_in']
#         check_out = data['check_out']
#         city_id = get_id_from_city(data['city'], cities_with_id)
#         params = {'check_in': check_in,
#                   'check_out': check_out,
#                   'currency': 'rub',
#                   'language': 'ru',
#                   # 'limit': '5',
#                   'type': 'popularity',
#                   'id': city_id,
#                   'token': TOKEN_AVIASALES}
#         data_info = requests.get(url, headers=headers, params=params).json()
#         print(data_info)
#     return render(request, "search_hotels.html", data_info)

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
        headers = {'Content-Type': 'application/json'}
        search_form = SearchHotelsForm(request.POST)
        if search_form.is_valid():
            city = search_form.cleaned_data['city']
            check_in = search_form.cleaned_data['check_in']
            check_out = search_form.cleaned_data['check_out']
            amount_guests = search_form.cleaned_data['amount_guests']
            print(city, check_in, check_out)
            city_id = get_id_from_city(city, cities_with_id)
            params = {'check_in': check_in,
                      'check_out': check_out,
                      'currency': 'rub',
                      'language': 'ru',
                      # 'limit': '5',
                      'type': 'popularity',
                      'id': city_id,
                      'token': TOKEN_AVIASALES}
            data_info = requests.get(url, headers=headers, params=params).json()

            data_info['amount_guests'] = int(amount_guests)
            print(data_info)
            # print(type(data_info['amount_guests']), amount_guests)
            return render(request, "search_hotels.html", {'form': search_form,
                                                          'today_date': today_date,
                                                          'data_info': data_info})  # pylint: disable=C0301
        else:  # pylint: disable=C0305
            return HttpResponse('Неверный формат введенных данных, повторите снова')
    else:
        search_form = SearchHotelsForm
        return render(request, "search_hotels.html", {'form': search_form, 'today_date': today_date})

