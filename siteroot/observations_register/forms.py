from django.contrib import auth
from django import forms
from .models import Patient, Questionnaire


class LoginForm(auth.forms.AuthenticationForm):

    error_messages = {
        'invalid_login': 'Неверное имя пользователя или пароль.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_required_attribute = False
        self.fields['username'].widget.attrs.pop("autofocus", None)


class PatientCreateForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('fullname', 'gender', 'birthday', 'eyes_col', 'hair_col')

class QuestionnaireCreateForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields =  ("date_of_visit","patient", "weight","growth","freckles","skin_col","redness_during_sunburn","tanning_character","rest_in_south","sunscreen_using",
        "neoplasm_appearance","neoplasm_location","skin_tumors_in_fam", "elem_size","elem_area","elem_borders","elem_color","inclusions","elem_symmetry")
