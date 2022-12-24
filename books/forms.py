
from django import forms
from . import models

class ShowForm(forms.ModelForm):
    class Meta:
        model = models.BOOKS
        fields = '__all__'