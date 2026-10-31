from django import forms
from .models import Booking
from django.contrib.auth.models import User




class Booking_form(forms.ModelForm):

    class Meta:
        model = Booking
        fields = [
            'phone',
            'item',
            'number_of_guests',
            'booking_date',
            'booking_time',
        ]

class Register_form(forms.Form):

    username = forms.CharField(max_length=150)

    password = forms.CharField(
        widget=forms.PasswordInput
    )

class Login_form(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput
    )

class BookingStatus_Form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']