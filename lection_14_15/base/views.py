from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dish, Event, Gallery
from .forms import UserReservationForm


def base(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    special = Dish.objects.filter(special=True)
    event = Event.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    reservation = UserReservationForm()

    data = {'categories': categories,
            'dishes': dishes,
            'specials': special,
            'events': event,
            'gallery': gallery,
            'reservation_form': reservation
            }

    return render(request, 'base.html', context=data)
