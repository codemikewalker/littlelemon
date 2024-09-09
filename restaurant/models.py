from django.db import models
import django.utils.timezone
# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateField()

class Menu(models.Model):
    ID = models.IntegerField( primary_key=True,)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
