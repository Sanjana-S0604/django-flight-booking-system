from django.db import models

# Create your models here.


class Flight(models.Model):
    company = models.CharField(max_length=50)
    flight_name = models.CharField(max_length=50)
    flight_no = models.IntegerField()
    from_city = models.CharField(max_length=50)
    to_city = models.CharField(max_length=50)
    departure = models.TimeField()
    date = models.DateField()
    price = models.IntegerField()

  


class Booking(models.Model):
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    aadhaar = models.CharField(max_length=12)
    age = models.IntegerField()

    seat_class = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=10)

   

# Create your models here.
