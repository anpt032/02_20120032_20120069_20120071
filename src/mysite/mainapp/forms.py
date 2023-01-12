from django import forms
from django.contrib.auth.models import User

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # check = forms.BooleanField(required=False)