from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
  return render(request, 'flights/index.html', {
    "flights": Flight.objects.all()
  })

def flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    return render(request, 'flights/flight.html', {
      "flight" : flight,
      "passengers": flight.passengers.all(),
      "non_passengers" : Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
  if request.method == "POST":
    flight = Flight.objects.get(pk=flight_id)
    passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
    passenger.flights.add(flight) # add a new row in table

    #redirect
    return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
    


