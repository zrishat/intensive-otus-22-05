from django.contrib import admin

# Register your models here.
from .models import Item, Avia, Hotel

admin.site.register(Item)
admin.site.register(Avia)
admin.site.register(Hotel)