from .models import Comment, CarAd
from django import forms




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CarForm(forms.ModelForm):
    
    """
    Form to add a Car
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