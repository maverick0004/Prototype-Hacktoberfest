from django import forms
from .models import Contributor

class ContributorForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Contributor
        fields = ['name']