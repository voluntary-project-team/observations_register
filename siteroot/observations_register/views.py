from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.views.generic import RedirectView
from django.urls import reverse
from django.views.generic.detail import DetailView
from .decorators import anonymous_required
from django.utils.decorators import method_decorator

#@method_decorator(anonymous_required, name='dispatch')
class IndexView(TemplateView):
    ''' Display index page '''
    template_name = f'index.html'

class AccountLoginView(LoginView):
    ''' Display the login form '''
    form_class = LoginForm
    template_name = f'login.html'
    redirect_authenticated_user = True

class ProfileRedirectView(RedirectView):
    ''' Redirect user to his profile '''
    def get_redirect_url(self, *args, **kwargs):
        return reverse(
            'profile-detail', args=[self.request.user.username]
        )

class ProfileDetailView(DetailView):
    ''' Display profile information '''
    template_name = f'profile.html'

    def get_object(self):
        return self.request.user