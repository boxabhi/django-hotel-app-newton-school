from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)