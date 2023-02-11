from .models import Comment, CarAd
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    """
    Form for User to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class CarForm(forms.ModelForm):
    """
    Form to add a Car
     """
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Car Name'
                }
            ),
        label='Name of Car'
    )

    number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone Number'
                }
            ),
        label='Phone Number'
    )

    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Price of Car'
                }
            ),
        label='Price Of Car in Euros'
    )

    year = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
                }
            ),
        label='Model Year'
    )

    nct = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
                }
            ),
        label='NCT Expiry'
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select Image of Car'
                }
            ),
        label='Image of Car'
    )

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
        self.fields['image'].label = ''