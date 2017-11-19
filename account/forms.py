from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('This user does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password')

        return super().clean()


class UserRegistrationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmed_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                         label='Confirm the password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', "confirmed_password"]

    def clean_password_confirm(self):

        password = self.cleaned_data.get('password')
        confirmed_password = self.cleaned_data.get('confirmed_password')
        if password != confirmed_password:
            raise forms.ValidationError('Passwords didn\'t match')

        return password

    def clean_email(self):

        email = self.cleaned_data.get('email')
        email_queryset = User.objects.filter(email=email)
        if email_queryset.exists() and email != '':
            raise forms.ValidationError('This email has already been registered')

        return email
