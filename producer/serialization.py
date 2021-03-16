from rest_framework.serializers import ModelSerializer
from producer.models import *


class CitySerializer(ModelSerializer):

    class Meta:
        model = CityModel
        fields = '__all__'

class StateSerializer(ModelSerializer):
    cities = CitySerializer(read_only=True,many=True)
    class Meta:
        model = StateModel
        fields = '__all__'

class CountrySerializer(ModelSerializer):
    states = StateSerializer(read_only=True,many=True)
    class Meta:
        model = CountryModel
        fields = '__all__'


