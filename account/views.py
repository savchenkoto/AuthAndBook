from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, RedirectView

from .forms import UserLoginForm, UserRegistrationForm


class LoginView(FormView):

    form_class = UserLoginForm
    template_name = 'form.html'
    success_url = '/home/books'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'bookshelf:books'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


class RegisterView(FormView):

    form_class = UserRegistrationForm
    success_url = '/home/books'
    template_name = 'form.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(self.request, user)
        return super().form_valid(form)
