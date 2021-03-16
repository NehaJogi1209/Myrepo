from django.contrib import admin
from django.urls import path
from consumer.tests import *


urlpatterns = [
    path('showall/', show_country_state_city),

]
