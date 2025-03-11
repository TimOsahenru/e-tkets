from django.contrib.auth.models import User
from django import forms

# Test clean_password2

class LoginForm(forms.Form):
    # username = forms.CharField()    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use')
        return data