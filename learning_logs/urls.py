from django.urls import path

from .import views

app_name= 'learning_logs'

urlpatterns= [
    path('',views.index, name='index'),
    path('topping',views.topping, name='topping'),
    path('toppings/,<int:topping_id>',views.toppings, name='toppings'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topping_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/,int:pizza_id>/', views.edit_entry, name='edit_entry')
]