from django.forms import ModelForm
from .models import *
from django import forms



class CommentForm(ModelForm):
    car = forms.ModelChoiceField(label='car',queryset=Cars.objects.all(),widget=forms.HiddenInput())
    class Meta:
        model = Comment
        fields = '__all__'



class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
