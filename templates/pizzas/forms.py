from django import forms
from .models import pizzas, topping

class TopicForm(forms.ModelForm):
    class Meta:
        model= pizzas
        fields= ['text']
        labels= {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = topping
        fields = ['text']
        labels = {'text': 'Topping:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}