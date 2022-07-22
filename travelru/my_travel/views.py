from django.shortcuts import render
from django.http import HttpResponseRedirect

from my_travel.models import Item, Hotel, Avia


# Create your views here.

def my_travel(request):
    my_travel_list = Item.objects.all().order_by('date_beg', 'time_beg')
    my_avia_list = Avia.objects.all()
    my_hotels_list = Hotel.objects.all()
    return render(request, 'my_travel.html', {'my_travel_list': my_travel_list,
                                              'my_hotels_list': my_hotels_list,
                                              'my_avia_list': my_avia_list,
                                              })


def delete_hotel_from_travel(request):
    print(request.POST)
    id = request.POST['hotel_id']
    hotel = Hotel.objects.get(id=id)
    print('hotel', hotel)
    hotel.delete()
    return HttpResponseRedirect('/my-travel')


def delete_avia_from_travel(request):
    id = request.POST['avia_id']
    avia = Avia.objects.get(id=id)
    print('avia', avia)
    avia.delete()
    return HttpResponseRedirect('/my-travel')
