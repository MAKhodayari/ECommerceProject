from django import forms


class ContactUsForm(forms.Form):
	# Remove init function and put its attrs in form definition
	form_email = forms.EmailField(required=True,
								  widget=forms.EmailInput(attrs={'class': 'form-control',
																 'placeholder': 'Your e-mail address'}))
	subject = forms.CharField(required=True, max_length=150,
							  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
	content = forms.CharField(required=True, max_length=450,
							  widget=forms.Textarea(attrs={'class': 'form-control',
														   'placeholder': 'Type your message here'}))
