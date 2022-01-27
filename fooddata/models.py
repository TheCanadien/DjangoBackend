from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    food_type = models.CharField(max_length=256, blank=False, null=False)
    kcal = models.IntegerField(blank=False, null=False)
    protein = models.FloatField(blank=False, null=False)
    carbohydrate = models.FloatField(blank=False, null=False)
    sugars = models.FloatField(blank=False, null=False)
    fiber = models.FloatField(blank=False, null=False)
    total_fat = models.FloatField(blank=False, null=False)
    saturated_fat = models.FloatField(blank=False, null=False)
    monounsaturated_fat = models.FloatField(blank=False, null=False)
    polyunsaturated_fat = models.FloatField(blank=False, null=False)
    def __str__(self):
        return self.food_type +" " + str(self.kcal) + " " +str(self.protein) + " " + str(self.carbohydrate) + " " + str(self.sugars) \
        + " " + str(self.fiber) + " " + str(self.total_fat) +  " " + str(self.saturated_fat) + " " + str(self.monounsaturated_fat)\
             + " " + str(self.polyunsaturated_fat) + "\n"



