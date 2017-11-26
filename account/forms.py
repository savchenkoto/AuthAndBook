from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')

        return super().clean()


class UserRegistrationForm(forms.ModelForm):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmed_password = forms.CharField(widget=forms.PasswordInput, label='Confirm the password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', "confirmed_password"]

    def clean_confirmed_password(self):
        password = self.cleaned_data.get('password')
        confirmed_password = self.cleaned_data.get('confirmed_password')
        if password != confirmed_password:
            raise forms.ValidationError('Password didn\'t match')

        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_queryset = User.objects.filter(email=email)
        if email_queryset.exists() and email != '':
            raise forms.ValidationError('This email has already been registered')

        return email
