from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from django import forms 
from .models import Customer


class SignupForm(UserCreationForm):

    username= forms.CharField(
        label= 'Username',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type': 'text'
        })
    )

    email= forms.EmailField(
        label= 'Email',
        widget= forms.EmailInput(attrs={
            'class' : 'form-control',
            'type': 'email'
        })
    )

    password1= forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'type': 'password'
        })
    )

    password2= forms.CharField(
        label= 'Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'type': 'password'
        })
    )
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2']


class CustomerModelForm(forms.ModelForm):

    Full_name= forms.CharField(
        label= 'Full Name',
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )
    locality= forms.CharField(
        label= 'Locality',
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )

    city= forms.CharField(
        label= 'City',
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )
    STATE= (
        ('Bihar', 'Bihar'),
        ('Delhi', 'Delhi'),
        ('West bengal', 'West bengal'),
        ('Punjab', 'Punjab'),
        ('UP', 'UP'),
    )
    state= forms.CharField(
        label= 'Select State',
        widget=forms.Select(attrs={
            'class' : 'form-control',
            
        }, choices=STATE)
    )

    zipcode= forms.IntegerField(
        label= 'Zip Code',
        widget=forms.NumberInput(attrs={
            'class' : 'form-control',
            'type' : 'number'
        })
    )

    phone= forms.IntegerField(
        label= 'Phone',
        widget=forms.NumberInput(attrs={
            'class' : 'form-control',
            'type' : 'number'
        })
    )
    class Meta:
        model = Customer
        fields= ['Full_name', 'locality', 'city', 'state', 'zipcode', 'phone']
        exclude= ['user']


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label= _('Old Password'),
        strip= False,
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'autocomplete' : 'current-password',
            'autofocus' : True

        })
    )

    new_password1 = forms.CharField(
        label= _('New Password'),
        strip= False,
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'autocomplete' : 'new-password',
          

        })
    )
    new_password2 = forms.CharField(
        label= _('Confirm New Password'),
        strip= False,
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'autocomplete' : 'new-password'
        })
    )
