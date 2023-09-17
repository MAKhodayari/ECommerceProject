from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# User = get_user_model()
from core.models import User
from core.validators import check_phone


class CustomerSignupForm(UserCreationForm):
	"""
	Using Django UserCreationForm as a form of registering customers.
	"""

	class Meta:
		model = User
		fields = ['phone', 'password1', 'password2']

	def clean_phone(self):
		"""
		Using phone validation to user input
		:return:
		"""
		phone = self.cleaned_data['phone']
		valid_phone = check_phone(phone)
		return valid_phone


class CustomerLoginForm(AuthenticationForm):
	"""
	Using Django AuthenticationForm as a form of signing customer in.
	"""
	# help_texts = {
	#     'username': _("Phone"),
	#     'password': _("Password"),
	# }
	#
	# def __init__(self, *args, **kwargs):
	#     super(CustomerLoginForm, self).__init__(*args, **kwargs)
	#     for field in self.fields.items():
	#         field[1].widget.attrs['placeholder'] = self.help_texts[field[0]]
