from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.views.generic import RedirectView, ListView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Patient
from django.contrib import messages
from .decorators import anonymous_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

#@method_decorator(anonymous_required, name='dispatch')
class IndexView(TemplateView):
    ''' Display index page '''
    template_name = f'index.html'

class AccountLoginView(LoginView):
    ''' Display the login form '''
    form_class = LoginForm
    template_name = f'login.html'
    redirect_authenticated_user = True

class AccountLogoutView(LogoutView):
    ''' Logout '''
    pass

class PatientsRedirectView(RedirectView):
    ''' Redirect user to list of patients '''
    def get_redirect_url(self, *args, **kwargs):
        return reverse('patients-detail')

class PatientsDetailView(ListView):
    ''' Display patients information '''
    model = Patient
    template_name = f'patients.html'
    context_object_name = 'patients'

    #def get_object(self):
    #    return self.request.user
