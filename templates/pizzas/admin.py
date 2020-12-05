from django.contrib import admin

# Register your models here.
from .models import pizzas,topping

admin.site.register(pizzas)
admin.site.register(topping)