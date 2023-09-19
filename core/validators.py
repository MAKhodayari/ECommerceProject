import re

from django.core.exceptions import ValidationError


def check_phone(value):
	"""
	Validate the phone number based on Iranian format
	:param: a string
	:return: True/False
	"""
	# Use one pattern for phone validation
	pattern = re.compile('^(9|09|00989|\\+989)(\\d{9})$')
	if pattern.match(value):
		return '0' + value[-10:]
	raise ValidationError(f'{value} is not a valid phone')
