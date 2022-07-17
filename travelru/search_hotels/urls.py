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

from search_hotels.views import search_hotels, add_to_travel

app_name = "search_hotels"

urlpatterns = [
    path("", search_hotels, name="search_hotels"),
    path("add/", add_to_travel, name="add_to_travel"),
#    path("my-travel/", my_travel, name="my_travel"),

]
