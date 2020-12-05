from django.contrib import admin

# Register your models here.
from .models import pizzas,topping

admin.site.register(pizza)
admin.site.register(topping)