# intensive-otus-22-05

http://create-travel.ru/ 

Инструкция для новых разработчиков

Для работы можно:
1) сделать форк к себе и делать пул реквесты на ветку develop, либо 
2) запросить доступ к репозиторию в телеграмме у @rishat_za для работы с ветками напрямую.

Склонировать репозиторий
`git clone https://github.com/zrishat/intensive-otus-22-05.git`

Основая ветка для разработки `develop`
Cоздать свою ветку
`git checkout -b new_feature`
После добавления своих изменений запушить коммиты в свою ветку и сделать PR на ветку develop.

К проекту подключены github actions. Необходимо покрывать код тестами, чтобы coverage не опускался иначе PR не пройдет проверку.
codestyle python - https://peps.python.org/pep-0008/

Для работы могут быть полезны такие переменные:
- DJANGO_DEBUG - True\False для вкл\выкл. режима дебага
- TOKEN_AVIASALES - токен можно взять у группы разработки, для работы с api
- TRAVELRU_SECRET_KEY - для прода

для бд
`python manage.py migrate`


Запуск локального сервера:
`python manage.py runserver`
