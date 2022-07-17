from django.shortcuts import render
from my_travel.models import Item

# Create your views here.
def my_travel(request):
    my_travel_list = Item.objects.all()
    return render(request, 'my_travel/my_travel.html', {'my_travel_list': my_travel_list})
