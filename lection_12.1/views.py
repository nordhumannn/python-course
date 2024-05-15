from django.shortcuts import render, HttpResponse


# Create your views here.
def manager(request):
    return HttpResponse('Manager page')


def menu(request):
    return HttpResponse('Menu page')


def events(request):
    return HttpResponse('Events page')


def booking(request):
    return HttpResponse('Booking page')
