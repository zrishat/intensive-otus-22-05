from django.shortcuts import render
import requests
# Create your views here.


# def index(request):
#     return render(request, "search_hotels.html")
from search_hotels.configuration_cities_hotels import cities_with_id
from travelru.settings import TOKEN_AVIASALES


def get_id_from_city(city_name: str, cities_list: list[dict]):
    for city in cities_list:
        if city['name'].lower() == city_name.lower():
            return city['id']


def search_hotels(request):
    data_info = {"popularity": ""}
    if request.method == "POST":
        url = 'http://yasen.hotellook.com/tp/public/widget_location_dump.json'
        headers = {'Content-Type': 'application/json'}
        data = request.POST
        print(data)
        check_in = data['check_in']
        check_out = data['check_out']
        city_id = get_id_from_city(data['city'], cities_with_id)
        params = {'check_in': check_in,
                  'check_out': check_out,
                  'currency': 'rub',
                  'language': 'ru',
                  # 'limit': '5',
                  'type': 'popularity',
                  'id': city_id,
                  'token': TOKEN_AVIASALES}
        data_info = requests.get(url, headers=headers, params=params).json()
        print(data_info)
    return render(request, "search_hotels.html", data_info)
