from django.contrib import admin

from .models import Category, Dish, Event, Gallery, UserReservation
admin.site.register(Category)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name', ), }


admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(UserReservation)
