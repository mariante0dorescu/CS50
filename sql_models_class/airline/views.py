from django.shortcuts import redirect

def redirect_to_flights(request):
    return redirect('flights:index')