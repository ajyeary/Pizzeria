from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    pizza = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def pizza(request, pizza_id):
    
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404

    entries = pizza.entry_set.order_by('-date_added')
    context = {'pizza': pizza, 'topping': Topping}
    return render(request, 'learning_logs/pizza.html', context)

@login_required
def new_pizza(request):
    """Add a new pizza."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_pizza.html', context)

@login_required
def new_topping(request, topic_id):
    """Add a new entry for a particular pizza."""
    pizza = pizza.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('learning_logs:pizza', pizza_id=pizza_id)

    context = {'pizza': pizza, 'form': form}
    return render(request, 'learning_logs/new_topping.html', context)




