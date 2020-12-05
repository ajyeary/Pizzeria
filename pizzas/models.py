from django.db import models

# Create your models here.
class pizzas(models.Model):
    pizza=models.CharField(max_length=200)
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.text

class topping(models.Model):
    pizza = models.ForeignKey(pizzas, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.text[:50]}..."
