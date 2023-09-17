from django.contrib import admin

from .models import *


class AddressShow(admin.ModelAdmin):
	"""
	Customizing appearance of addresses on admin panel.
	"""
	search_fields = ['street']
	ordering = ['country']
	list_per_page = 15


class CustomerShow(admin.ModelAdmin):
	"""
	Customizing appearance of customers on admin panel.
	"""
	list_display = ['user', 'phone', 'name']
	search_fields = ['user', 'phone', 'name']
	ordering = ['user', ]
	list_per_page = 15


admin.site.register(Address, AddressShow)
admin.site.register(Customer, CustomerShow)
# Registering models to admin panel
