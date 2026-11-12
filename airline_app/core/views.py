from django.shortcuts import render, redirect, get_object_or_404
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
                booking = Booking.objects.create(
                    passenger_name=name,
                    passenger_email=email,
                    flight=flight,
                    seat_number=seat
                )
                flight.available_seats -= 1
                flight.save()
                
                # Booking complete hote hi user ko direct ticket receipt page par redirect karein
                return redirect('ticket_view', booking_id=booking.id)
                
        except Flight.DoesNotExist:
            pass
            
        return redirect('index')

    context = {
        'flights': flights,
        'origins': sorted(list(origins)),
        'destinations': sorted(list(destinations)),
    }
    
    return render(request, 'core/index.html', context)


def ticket_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        'booking': booking,
    }
    return render(request, 'core/ticket.html', context)