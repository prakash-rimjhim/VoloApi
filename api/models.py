from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.CharField(max_length= 50)
    department = models.CharField(max_length= 50)
    Software = models.CharField(max_length= 50)
    seats = models. IntegerField()
    Amount = models.IntegerField()