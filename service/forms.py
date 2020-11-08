from django import forms
from .models import *

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('status','user_id',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


