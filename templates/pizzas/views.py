from django.shortcuts import render, redirect
from .models import pizzas, topping
# Create your views here.

def index(request):
    return render(request, 'Pizzas/index.html')

def pizza(request, pizza_id):
    pizza=pizza.objects.get(id=pizza_id)
    toppings= {'pepperoni':topping, 'mushrooms':topping}
    return render(request,'pizzas/pizza.html', context)

def new_pizza(request):
    if request.method !='POST':
        form= TopicForm()
    else:
        form= TopicForm(data=request.POST)
        if form.is_valid():
            new_pizza= form.save(commit=False)
    context={'form': form}
    return render(request,'pizzas/new_pizza.html',context)



