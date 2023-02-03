from .models import Comment, CarAd
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CarForm(forms.ModelForm):
    
    """
    Form to add a recipe
     """
    class Meta:
        model = CarAd
        fields = [
            'title',
            'image',
            'number',
            'nct',
            'year',
            'price',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)