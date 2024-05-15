from django.urls import path
from .views import manager, menu, events, booking

urlpatterns = [
    path('menu/', menu),
    path('events/', events),
    path('booking/', booking),
    path('', manager),
]
