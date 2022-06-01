"""travelRu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import search_avia_page, search_train_page, index, search_avia_tickets

app_name = "waySearch"

urlpatterns = [
    path("", index, name="index"),
    path("search_avia/", search_avia_page, name="search_avia"),
    path('search_avia/tickets', search_avia_tickets, name='search_avia_tickets'),
    path("search_train/", search_train_page, name="search_train"),
]
