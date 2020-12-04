from django.urls import path

from .import views

app_name= 'learning_logs'

urlpatterns= [
    path('',views.index, name='index'),
    path('topping',views.topping, name='topping'),
    path('toppings/,<int:topping_id>',views.toppings, name='toppings'),
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    path('new_topping/<int:topping_id>/', views.new_topping, name='new_topping'),
    path('edit_topping/,int:pizza_id>/', views.edit_topping, name='edit_topping')
]