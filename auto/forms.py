from .models import Comment, CarAd
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
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
        label=''
    )

    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Price of Car'
                }
            ),
        label='Price Of Car'
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
                }
            ),
        label=''
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