from django.contrib.auth.forms import UserCreationForm

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

# Remove unused customized customer login form
