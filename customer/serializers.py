from rest_framework import serializers

# Better imports
from customer.models import *


class AddressSerializer(serializers.ModelSerializer):
	"""
	Address model serializer
	"""
	class Meta:
		model = Address
		fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
	"""
	Customer model serializer
	"""
	class Meta:
		model = Customer
		fields = '__all__'
