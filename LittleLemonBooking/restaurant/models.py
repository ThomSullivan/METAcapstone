from django.db import models

# Create your models here.
class Booking(models.Model):
    class GuestSelector(models.IntegerChoices):
        one = 1, 'Single person'
        two = 2, 'Two people'
        three = 3, 'Three people'
        four = 4, 'Four people'
        five = 5, 'Five people'
        six = 6, 'Six people'

    name = models.CharField(max_length=255)
    No_of_guests = models.PositiveSmallIntegerField(choices=GuestSelector.choices, default=GuestSelector.one)
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'