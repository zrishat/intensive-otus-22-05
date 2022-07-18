from django.shortcuts import render
from django.http import HttpResponseRedirect

from my_travel.models import Item


# Create your views here.

def my_travel(request):
    my_travel_list = Item.objects.all().order_by('date_beg', 'time_beg')
    return render(request, 'my_travel/my_travel.html', {'my_travel_list': my_travel_list})


def delete_hotel_from_travel(request):
    id = request.POST['id']
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/my-travel')
