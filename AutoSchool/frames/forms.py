from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
# Форма отправки заявки
    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'password']