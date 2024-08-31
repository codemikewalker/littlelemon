from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(max_length=6)
    booking_date = models.DateField()

class Menu(models.Model):
    ID = models.IntegerField( primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    inventory = models.IntegerField()
