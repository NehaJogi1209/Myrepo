from django.db import models


# Create your models here.
class CountryModel(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=50)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'COUNTRY'



class StateModel(models.Model):
    sid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=50)
    country = models.ForeignKey('CountryModel',on_delete= models.CASCADE,related_name='states',null=False)

    def __str__(self):
        return self.state

    class Meta:
        db_table = 'STATE'

class CityModel(models.Model):
    ctid = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50)
    state = models.ForeignKey('StateModel', on_delete=models.CASCADE, related_name='cities', null=False)

    def __str__(self):
        return self.city

    class Meta:
        db_table = 'CITY'


