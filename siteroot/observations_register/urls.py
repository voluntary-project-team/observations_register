from django.urls import path
from  .views import *

urlpatterns = [
    path('', AccountLoginView.as_view(), name='account-login'),
    path('logout', AccountLogoutView.as_view(), name='account-logout'),
    path('redirect', PatientsRedirectView.as_view(), name='patients-redirect'),
    path('patients', PatientsDetailView.as_view(), name='patients-detail'),
    path('delete/<patient_id>', delete_patient, name='delete')
]