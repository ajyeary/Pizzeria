import os
os.environ.setdefault("DJANGO_SETTINGS_MODEULE","learning_log.settings")

import django
django.setup()

from Pizzas.model import Pizza

Pizza= Pizza.objects.all()

for Pizza in Pizzas:
    print("Pizza ID:", Pizza.id, "Pizza:", Pizza)


t= Pizza.objects.get(id=1)
print(t.text)
print(t.date_added)

topping= t.toppings_set.all()

for toppings in topping:
    print(toppings)
    