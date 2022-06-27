from .models import *

from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        # fields = []
        exclude = ['create_date']
