from django.contrib import admin
from django.urls import path
from producer.views import *


urlpatterns = [
    path('countries', CountryApiView.as_view(), name='countries'),
    path(':country/states', StateApiView.as_view(), name='states'),
    path(':country/:states/cities', CityApiView.as_view(), name='cities'),
]
