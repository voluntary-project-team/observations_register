from django.urls import path
from  .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AccountLoginView.as_view(), name='account-login'),
    path('logout', AccountLogoutView.as_view(), name='account-logout'),
    path('redirect', PatientsRedirectView.as_view(), name='patients-redirect'),
    path('patients', PatientsDetailView.as_view(), name='patients-detail'),
    path('delete/<patient_id>', delete_patient, name='delete'),
    path('medical_card/<patient_id>', MedicalCardDetailView.as_view(), name='medical-card'),
    path('medical_card/<patient_id>/patient-update', PatientUpdateView.as_view(), name='patient-update'),
    path('medical_card/<patient_id>/create-questionnaire', CreateQuestionnaire.as_view(), name='create-questionnaire'),
    path('delete-questionnaire/<patient_id>/<questionnaire_id>', delete_questionnaire, name='delete-questionnaire'),
    path('export-patient',  PatientExportView.as_view(), name='export_patient'),
    path('export-questionnaire',  QuestionnaireExportView.as_view(), name='export_questionnaire'),
    path('import-patient', import_patient, name='import_patient'),
    path('import-questionnare', import_questionnaire, name='import_questionnaire'),
    path('medical_card/<patient_id>/<questionnaire_id>/questionnaire-update', QuestionnaireUpdateView.as_view(), name='questionnaire-update')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)