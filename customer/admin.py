from django.contrib import admin

# Better import
from customer.models import *


# Model registration at the beginning
@admin.register(Address)
class AddressShow(admin.ModelAdmin):
	"""
	Customizing appearance of addresses on admin panel.
	"""
	search_fields = ['street']
	ordering = ['country']
	list_per_page = 15


# Model registration at the beginning
@admin.register(Customer)
class CustomerShow(admin.ModelAdmin):
	"""
	Customizing appearance of customers on admin panel.
	"""
	list_display = ['user', 'phone', 'name']
	search_fields = ['user', 'phone', 'name']
	ordering = ['user']
	list_per_page = 15
