from django.db import models

#Create your models

class Bowler(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    countryName = models.CharField(max_length=250)
    country_flag = models.CharField(max_length=100)
    over_played = models.IntegerField()


class Batsman(models.Model):
    bowler = models.ForeignKey(Bowler,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    run_rate = models.IntegerField()