from django.shortcuts import render
import requests

def show_country_state_city(request):
    response = requests.get('http://127.0.0.1:8000/prod/countries')
    countrydata = response.json()
    response = requests.get('http://127.0.0.1:8000/prod/:country/states')
    statedata = response.json()
    response = requests.get('http://127.0.0.1:8000/prod/:country/:states/cities')
    citydata = response.json()
    return render(request, 'dashboard.html', {"countrydata": countrydata,"statedata":statedata,"citydata":citydata})