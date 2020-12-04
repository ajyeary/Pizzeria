from django import forms
from .models import Pizza, Topping

class TopicForm(forms.ModelForm):
    class Meta:
        model= Pizza
        fields= ['text']
        labels= {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['text']
        labels = {'text': 'Topping:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
