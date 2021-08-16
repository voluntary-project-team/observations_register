from django.urls import path
from  .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', AccountLoginView.as_view(), name='account-login'),
    path('logout', AccountLogoutView.as_view(), name='account-logout'),
    path('redirect', PatientsRedirectView.as_view(), name='patients-redirect'),
    path('patients', PatientsDetailView.as_view(), name='patients-detail'),
]