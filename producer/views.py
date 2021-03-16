from django.shortcuts import render
from producer.models import *
from producer.serialization import *
from rest_framework.response import Response
from rest_framework.views import APIView

class CountryApiView(APIView):
    def get(self,request,format=None):
        countries = CountryModel.objects.all()
        serializaionobj = CountrySerializer(countries, many=True)
        return Response(serializaionobj.data)


class StateApiView(APIView):
    def get(self, request, format=None):
        states = StateModel.objects.all()
        serializaionobj = StateSerializer(states, many=True)
        return Response(serializaionobj.data)


class CityApiView(APIView):
    def get(self, request, format=None):
        cities = CityModel.objects.all()
        serializaionobj = CitySerializer(cities, many=True)
        return Response(serializaionobj.data)



