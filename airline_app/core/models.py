from django.db import models

class Flight(models.Model):
    STATUS_CHOICES = [
        ('On Time', 'On Time'),
        ('Boarding', 'Boarding'),
        ('Delayed', 'Delayed'),
    ]

    flight_number = models.CharField(max_length=20, unique=True)
    source = models.CharField(max_length=100)        # Extended for global city/airport names
    destination = models.CharField(max_length=100)   # Extended for global city/airport names
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField(default=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Time') # Added status field

    def __str__(self):
        return f"{self.flight_number}: {self.source} -> {self.destination} ({self.status})"

class Booking(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight.flight_number}"