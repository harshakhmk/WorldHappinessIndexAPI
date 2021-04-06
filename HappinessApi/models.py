from django.db import models

# Create your models here.

class Country(models.Model):
    CountryName=models.CharField(max_length=60,db_index=True)
    Rank=models.IntegerField(default=1,null=True)
    LadderScore=models.FloatField(db_index=True)
    HealthyLifeExpectancy=models.FloatField()
    Generosity=models.FloatField()
    Gdp =models.FloatField()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Rank=self.id

    def __str__(self):
        return self.CountryName