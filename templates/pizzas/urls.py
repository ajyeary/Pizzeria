from django.urls import path

from . import views

app_name= 'pizzas'

urlpatterns= [
    path('',views.index, name='index'),
    path('pizzas', views.pizza,name='pizzas'),
    path('topping', views.topping, name='topping'),
    path('new_pizza/', views.new_pizza, name='new_pizza'),

]