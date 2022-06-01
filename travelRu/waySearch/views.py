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
    data_cities = (
        {"city": "Абакан", "airport": "Абакан", "iata": "ABA"},
        {"city": "Алдан", "airport": "Алдан", "iata": "ADH"},
        {"city": "Амдерма", "airport": "Амдерма", "iata": "AMV"},
        {"city": "Анадырь", "airport": "Угольный", "iata": "DYR"},
        {"city": "Анапа", "airport": "Витязево", "iata": "AAQ"},
        {"city": "Апатиты", "airport": "Апатиты-Кировск", "iata": "KVK"},
        {"city": "Архангельск", "airport": "Талаги", "iata": "ARH"},
        {"city": "Астрахань", "airport": "Астрахань", "iata": "ASF"},
        {"city": "Ачинск", "airport": "Ачинск", "iata": "ACS"},
        {"city": "Барнаул", "airport": "Барнаул", "iata": "BAX"},
        {"city": "Белгород", "airport": "Белгород", "iata": "EGO"},
        {"city": "Белорецк", "airport": "Белорецк", "iata": "BCX"},
        {"city": "Благовещенск", "airport": "Игнатьево", "iata": "BQS"},
        {"city": "Бор", "airport": "Подкаменная Тунгуска", "iata": "TGP"},
        {"city": "Братск", "airport": "Братск", "iata": "BTK"},
        {"city": "Брянск", "airport": "Брянск", "iata": "BZK"},
        {"city": "Бугульма", "airport": "Бугульма", "iata": "UUA"},
        {"city": "Великие Луки", "airport": "Великие Луки", "iata": "VLU"},
        {"city": "Великий Устюг", "airport": "Великий Устюг", "iata": "VUS"},
        {"city": "Владивосток", "airport": "Кневичи", "iata": "VVO"},
        {"city": "Владикавказ", "airport": "Беслан", "iata": "OGZ"},
        {"city": "Волгоград", "airport": "Гумрак", "iata": "VOG"},
        {"city": "Вологда", "airport": "Вологда", "iata": "VGD"},
        {"city": "Воркута", "airport": "Воркута", "iata": "VKT"},
        {"city": "Воронеж", "airport": "Чертовицкое", "iata": "VOZ"},
        {"city": "Геленджик", "airport": "Геленджик", "iata": "GDZ"},
        {"city": "Грозный", "airport": "Грозный", "iata": "GRV"},
        {"city": "Диксон", "airport": "Диксон", "iata": "DKS"},
        {"city": "Екатеринбург", "airport": "Кольцово", "iata": "SVX"},
        {"city": "Енисейск", "airport": "Енисейск", "iata": "EIE"},
        {"city": "Иваново", "airport": "Иваново-Южный", "iata": "IWA"},
        {"city": "Игарка", "airport": "Игарка", "iata": "IAA"},
        {"city": "Ижевск", "airport": "Ижевск", "iata": "IJK"},
        {"city": "Инта", "airport": "Инта", "iata": "INA"},
        {"city": "Иркутск", "airport": "Иркутск", "iata": "IKT"},
        {"city": "Йошкар-Ола", "airport": "Йошкар-Ола", "iata": "JOK"},
        {"city": "Казань", "airport": "Казань", "iata": "KZN"},
        {"city": "Калининград", "airport": "Храброво", "iata": "KGD"},
        {"city": "Кемерово", "airport": "Кемерово", "iata": "KEJ"},
        {"city": "Киров", "airport": "Победилово", "iata": "KVX"},
        {"city": "Когалым", "airport": "Когалым", "iata": "KGP"},
        {"city": "Комсомольск-на-Амуре", "airport": "Хурба", "iata": "KXK"},
        {"city": "Кострома", "airport": "Сокеркино", "iata": "KMW"},
        {"city": "Котлас", "airport": "Котлас", "iata": "KSZ"},
        {"city": "Краснодар", "airport": "Пашковский", "iata": "KRR"},
        {"city": "Красноярск", "airport": "Емельяново", "iata": "KJA"},
        {"city": "Курган", "airport": "Курган", "iata": "KRO"},
        {"city": "Курильск", "airport": "Буревестник", "iata": "BVV"},
        {"city": "Курск", "airport": "Восточный", "iata": "URS"},
        {"city": "Кызыл", "airport": "Кызыл", "iata": "KYZ"},
        {"city": "Лешуконское", "airport": "Лешуконское", "iata": "LDG"},
        {"city": "Липецк", "airport": "Липецк", "iata": "LPK"},
        {"city": "Магадан", "airport": "Сокол", "iata": "GDX"},
        {"city": "Магдагачи", "airport": "Магдагачи", "iata": "GDG"},
        {"city": "Магнитогорск", "airport": "Магнитогорск", "iata": "MQF"},
        {"city": "Махачкала", "airport": "Уйташ", "iata": "MCX"},
        {"city": "Минеральные Воды", "airport": "Минеральные Воды", "iata": "MRV"},
        {"city": "Мирный", "airport": "Мирный", "iata": "MJZ"},
        {"city": "Москва", "airport": "Шереметьево", "iata": "MOW"},
        {"city": "Москва", "airport": "Быково", "iata": "BKA"},
        {"city": "Москва", "airport": "Внуково", "iata": "VKO"},
        {"city": "Москва", "airport": "Домодедово", "iata": "DME"},
        {"city": "Мурманск", "airport": "Мурманск", "iata": "MMK"},
        {"city": "Надым", "airport": "Надым", "iata": "NYM"},
        {"city": "Нальчик", "airport": "Нальчик", "iata": "NAL"},
        {"city": "Нарьян-Мар", "airport": "Нарьян-Мар", "iata": "NNM"},
        {"city": "Нерюнгри", "airport": "Чульман", "iata": "CNN"},
        {"city": "Нижневартовск", "airport": "Нижневартовск", "iata": "NJC"},
        {"city": "Нижнекамск", "airport": "Бегишево", "iata": "NBC"},
        {"city": "Нижний Новгород", "airport": "Стригино", "iata": "GOJ"},
        {"city": "Новокузнецк", "airport": "Спиченково", "iata": "NOZ"},
        {"city": "Новосибирск", "airport": "Толмачёво", "iata": "OVB"},
        {"city": "Новый Уренгой", "airport": "Новый Уренгой", "iata": "NUX"},
        {"city": "Ноглики", "airport": "Ноглики", "iata": "NGL"},
        {"city": "Норильск", "airport": "Алыкель", "iata": "NSK"},
        {"city": "Ноябрьск", "airport": "Ноябрьск", "iata": "NOJ"},
        {"city": "Октябрьский", "airport": "Октябрьский", "iata": "OKT"},
        {"city": "Омск", "airport": "Омск-Центральный", "iata": "OMS"},
        {"city": "Орёл", "airport": "Орёл-Южный", "iata": "OEL"},
        {"city": "Оренбург", "airport": "Оренбург-Центральный", "iata": "REN"},
        {"city": "Орск", "airport": "Орск", "iata": "OSW"},
        {"city": "Оха", "airport": "Оха", "iata": "OHH"},
        {"city": "Охотск", "airport": "Охотск", "iata": "OHO"},
        {"city": "Певек", "airport": "Певек", "iata": "PWE"},
        {"city": "Пенза", "airport": "Пенза", "iata": "PEZ"},
        {"city": "Пермь", "airport": "Большое Савино", "iata": "PEE"},
        {"city": "Петрозаводск", "airport": "Бесовец", "iata": "PES"},
        {"city": "Петропавловск-Камчатский", "airport": "Елизово", "iata": "PKC"},
        {"city": "Печора", "airport": "Печора", "iata": "PEX"},
        {"city": "Провидения", "airport": "Бухта Провидения", "iata": "PVS"},
        {"city": "Псков", "airport": "Псков", "iata": "PKV"},
        {"city": "Радужный", "airport": "Радужный", "iata": "RAT"},
        {"city": "Ростов-на-Дону", "airport": "Ростов-на-Дону", "iata": "ROV"},
        {"city": "Рыбинск", "airport": "Староселье", "iata": "RYB"},
        {"city": "Рязань", "airport": "Дягилево", "iata": "RZN"},
        {"city": "Рязань", "airport": "Турлатово", "iata": "RZN"},
        {"city": "Салехард", "airport": "Салехард", "iata": "SLY"},
        {"city": "Самара", "airport": "Курумоч", "iata": "KUF"},
        {"city": "Санкт-Петербург", "airport": "Пулково", "iata": "LED"},
        {"city": "Саранск", "airport": "Саранск", "iata": "SKX"},
        {"city": "Саратов", "airport": "Саратов-Центральный", "iata": "RTW"},
        {"city": "Смоленск", "airport": "Смоленск-Южный", "iata": "LNX"},
        {"city": "Советская Гавань", "airport": "Май-Гатка", "iata": "GVN"},
        {"city": "Соловецкие острова", "airport": "Соловки", "iata": "CSH"},
        {"city": "Сочи", "airport": "Адлер-Сочи", "iata": "AER"},
        {"city": "Ставрополь", "airport": "Шпаковское", "iata": "STW"},
        {"city": "Сургут", "airport": "Сургут", "iata": "SGC"},
        {"city": "Сыктывкар", "airport": "Сыктывкар", "iata": "SCW"},
        {"city": "Тамбов", "airport": "Донское", "iata": "TBW"},
        {"city": "Тикси", "airport": "Тикси", "iata": "IKS"},
        {"city": "Тобольск", "airport": "Тобольск", "iata": "TOX"},
        {"city": "Томск", "airport": "Богашёво", "iata": "TOF"},
        {"city": "Тында", "airport": "Тында", "iata": "TYD"},
        {"city": "Тюмень", "airport": "Рощино", "iata": "TJM"},
        {"city": "Удачный", "airport": "Полярный", "iata": "PYJ"},
        {"city": "Улан-Удэ", "airport": "Байкал", "iata": "UUD"},
        {"city": "Ульяновск", "airport": "Баратаевка", "iata": "ULY"},
        {"city": "Усть-Кут", "airport": "Усть-Кут", "iata": "UKX"},
        {"city": "Усинск", "airport": "Усинск", "iata": "USK"},
        {"city": "Уфа", "airport": "Уфа", "iata": "UFA"},
        {"city": "Ухта", "airport": "Ухта", "iata": "UCT"},
        {"city": "Хабаровск", "airport": "Хабаровск-Новый", "iata": "KHV"},
        {"city": "Ханты-Мансийск", "airport": "Ханты-Мансийск", "iata": "HMA"},
        {"city": "Хатанга", "airport": "Хатанга", "iata": "HTG"},
        {"city": "Цимлянск", "airport": "Волгодонск", "iata": "VLK"},
        {"city": "Чебоксары", "airport": "Чебоксары", "iata": "CSY"},
        {"city": "Челябинск", "airport": "Челябинск", "iata": "CEK"},
        {"city": "Череповец", "airport": "Череповец", "iata": "CEE"},
        {"city": "Черский", "airport": "Черский", "iata": "CYX"},
        {"city": "Чита", "airport": "Кадала", "iata": "HTA"},
        {"city": "Чокурдах", "airport": "Чокурдах", "iata": "CKH"},
        {"city": "Шахтерск", "airport": "Шахтерск", "iata": "EKS"},
        {"city": "Щёлково", "airport": "Чкаловский", "iata": "CKL"},
        {"city": "Элиста", "airport": "Элиста", "iata": "ESL"},
        {"city": "Южно-Курильск", "airport": "Менделеево", "iata": "DEE"},
        {"city": "Южно-Сахалинск", "airport": "Хомутово", "iata": "UUS"},
        {"city": "Якутск", "airport": "Якутск", "iata": "YKS"},
        {"city": "Ярославль", "airport": "Туношна", "iata": "IAR"})
    for city in data_cities:
        if city['city'] == code:
            return city['iata']
    return ""
