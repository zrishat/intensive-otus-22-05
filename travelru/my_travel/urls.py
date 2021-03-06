"""travelru URL Configuration

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
# pylint: disable=invalid-name

from django.urls import path

from my_travel.views import my_travel, delete_hotel_from_travel, delete_avia_from_travel

app_name = "my_travel"

urlpatterns = [
    path("", my_travel, name="my_travel"),
    path("delete_hotel/", delete_hotel_from_travel, name="delete_hotel_from_travel"),
    path("delete_avia/", delete_avia_from_travel, name="delete_avia_from_travel"),
]
