from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'gender', 'venue']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose'}),
            'venue': forms.Select(attrs={'class': 'form-control'}),
        }
