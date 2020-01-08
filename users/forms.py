from PIL import Image
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import TextInput, PasswordInput, DateInput
from django.utils.translation import ugettext_lazy as _
from users.models import User, phone, District, Employee


class TelInput(TextInput):
    input_type = 'tel'


class HiddenSelectInput(forms.Select):
    input_type = 'hidden'


class UserLoginForm(forms.Form):
    number = forms.CharField(validators=[phone],
                             widget=TelInput(
                                 attrs={'class': 'col-12 form-control-sm masked', 'placeholder': '550XXXXXX',
                                        'pattern': '^\d{9}$'}),
                             required=True, help_text=_('This field required'), label=_('number'))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'col-12 form-control-sm'}), required=True,
                               help_text=_('Password required'), label=_('password'))
    next = forms.CharField(widget=TextInput(attrs={'hidden': True}), required=False)

    class Meta:
        fields = ['number', 'password', 'next']


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['qrcode', 'agreement', 'login', 'password', 'district']
