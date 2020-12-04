from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    name = models.CharField(primary_key=True,max_length=200)

    def __str__(self):
        
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural= 'toppings'
 
    def __str__(self):
        return f"{self.text[:50]}..."





  
