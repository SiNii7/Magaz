from django import forms
from django.forms import Form
# from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea
from app.models import Profile

class UserForm(UserCreationForm):
    username = forms.CharField(label='Login',
                               help_text='')
    password1 = forms.CharField(label='Пароль',
                    help_text='',
                    widget=forms.PasswordInput(
                        attrs={'autocomplete':'new-password'}
                    ))
    password2 = forms.CharField(label='Подтверждение',
                    help_text='',
                    widget=forms.PasswordInput(
                        attrs={'autocomplete':'new-password'}
                    ))
    email = forms.EmailField(label='Почта',
                    widget=forms.TextInput(
                        attrs={'placeholder':'qwe@mail.ru'}))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    # captcha = CaptchaField()


class OrderForm(Form):
    adres = forms.CharField(label='Адрес доставки')
    email = forms.EmailField(label='Email')
    telephone = forms.CharField(label='Telephone')

