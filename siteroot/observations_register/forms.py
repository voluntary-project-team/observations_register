from django.contrib import auth


class LoginForm(auth.forms.AuthenticationForm):

    error_messages = {
        'invalid_login': 'Неверное имя пользователя или пароль.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_required_attribute = False
        self.fields['username'].widget.attrs.pop("autofocus", None)