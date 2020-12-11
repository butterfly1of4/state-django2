from django import forms
from .models import Capitals


class CapitalForm(forms.ModelForm):

    class Meta:
        model = Capitals
        fields = ('state', 'capital')
