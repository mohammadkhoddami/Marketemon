from django import forms
from .models import User, OptCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confrim password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone_number')

    def clean_password2(self):
        cd = self.changed_data
        
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('Passwords must be match')
        return cd['password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    

class UserChangeForm(forms.ModelForm):
    """
    Using ReadOnlyPassowrdHashField for not letting user change password directly
    instead giving user a form to change his password (all this operations is on admin panel)

    """
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\"> this form</a>.")

    class Meta: 
        model = User 
        fields = ('email', 'password', 'phone_number', 'fullname', 'last_login')


class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    fullname = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError('This Phone Number Is Already Exist')
        OptCode.objects.filter(phone=phone_number).delete()
        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email is Already Exist')
        
        return email


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()


class UserLoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
