from django.contrib import admin
from producer.models import *
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ['cid','cname']
admin.site.register(CountryModel,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ['sid','state','country']
admin.site.register(StateModel,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['ctid','city','state']
admin.site.register(CityModel,CityAdmin)