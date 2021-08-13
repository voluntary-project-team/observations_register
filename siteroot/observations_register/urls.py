from django.urls import path
from  .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', AccountLoginView.as_view(), name='account-login'),
    path('redirect', ProfileRedirectView.as_view(), name='profile-redirect'),
    path('<slug:username>', ProfileDetailView.as_view(), name='profile-detail'),
]