from django.shortcuts import render, redirect
from .models import Flight, Booking

def index(request):
    flights = Flight.objects.all()
    
    # Database ki flights se unique origins aur destinations extract karna
    origins = Flight.objects.values_list('source', flat=True).distinct()
    destinations = Flight.objects.values_list('destination', flat=True).distinct()

    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        seat = request.POST.get('seat')
        
        try:
            flight = Flight.objects.get(id=flight_id)
            if flight.available_seats > 0:
                Booking.objects.create(
                    passenger_name=name,
                    passenger_email=email,
                    flight=flight,
                    seat_number=seat
                )
                flight.available_seats -= 1
                flight.save()
        except Flight.DoesNotExist:
            pass
            
        return redirect('index')

    context = {
        'flights': flights,
        'origins': sorted(list(origins)),
        'destinations': sorted(list(destinations)),
    }
    
    return render(request, 'core/index.html', context)