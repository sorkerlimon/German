from django.db import models

# Create your models here.
class Country(models.Model):

    c_name = models.CharField(max_length=200, unique=True,primary_key=True)
  
    def __str__(self):
        return f'{str(self.c_name)}'


class Location(models.Model):
    c_name = models.ForeignKey(Country,null=True,blank=True,on_delete=models.CASCADE)
    l_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{str(self.c_name)} : {str(self.l_name)}'


class BusinessPlan(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value1 = models.PositiveIntegerField()
    value2 = models.PositiveIntegerField()
    value3 = models.PositiveIntegerField()


    def __str__(self):
        return f'{str(self.location)} : {str(self.name)} : {str(self.value1)} : {str(self.value2)} : {str(self.value3)}'

class SelectedPlan(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    business_plan = models.ForeignKey(BusinessPlan, on_delete=models.CASCADE)
    value1 = models.PositiveIntegerField()
    value2 = models.PositiveIntegerField()
    value3 = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.country} - {self.location} - {self.business_plan}'
