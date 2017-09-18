from django import forms
from django.forms import ModelForm

from .models import NewEmployee



class NewEmployeeForm(ModelForm):
	class Meta:
		model = NewEmployee
		fields = ['name', 'location']
