from django import forms
from django.core.exceptions import ValidationError


from app_database.models import Book


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control'}),
		'pages': forms.NumberInput(attrs={'class': 'form-control'}),
		'description': forms.TextInput(attrs={'class': 'form-control'}),
		'author': forms.TextInput(attrs={'class': 'form-control'})
		}


class FormCalculator(forms.Form):
	number_one = forms.FloatField()
	number_two = forms.FloatField()
	widgets = {
	'number_one': forms.NumberInput(attrs={'class': 'form-control'}),
	'number_two': forms.NumberInput(attrs={'class': 'form-control'})
	}

	def clean(self):
		if not isinstance(self.cleaned_data['number_one'], float or int):
			raise ValidationError('Must be a number!')
		if not isinstance(self.cleaned_data['number_two'], float or int):
			raise ValidationError('Must be a number!')
		if self.cleaned_data['number_one'] < 0:
			raise ValidationError('Number cannot be less than zero!')
		if self.cleaned_data['number_two'] < 0:
			raise ValidationError('Number cannot be less than zero!')

		return self.cleaned_data

