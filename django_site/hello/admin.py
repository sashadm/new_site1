from django.contrib import admin

#from .models import Human
from .models import *

#admin.site.register(Human)
admin.site.register(CarColor)
admin.site.register(CarMark)
admin.site.register(CarModel)
admin.site.register(Comment)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['mark','model','color']
    list_filter = ['color','mark']


admin.site.register(Cars,CarsAdmin)
