from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from braces.views import AnonymousRequiredMixin
from . import forms, models


class SignUp(AnonymousRequiredMixin, CreateView):
    form_class = forms.EmailUserCreationForm
    template_name = 'user/signup.html'
    model = models.EmailUser
    success_url = settings.SIGNUP_REDIRECT

    def form_valid(self, form):
        response = super(SignUp, self).form_valid(form)
        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return response
