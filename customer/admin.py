from django.contrib import admin

# Better import
from core.admin import BaseModelAdmin
from customer.models import *


# Model registration at the beginning
@admin.register(Address)
class AddressShow(BaseModelAdmin):
	"""
	Customizing appearance of addresses on admin panel.
	"""
	search_fields = ['street']
	ordering = ['country']


# Model registration at the beginning
@admin.register(Customer)
class CustomerShow(BaseModelAdmin):
	"""
	Customizing appearance of customers on admin panel.
	"""
	list_display = ['user', 'phone', 'name']
	search_fields = ['user', 'phone', 'name']
	ordering = ['user']
