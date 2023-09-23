from django.contrib import admin

# Better import
from core.admin import BaseModelAdmin
from product.models import *


# Register first
@admin.register(Category)
class CategoryShow(BaseModelAdmin):
	"""
	An admin model class for costuming categories on admin panel.
	"""
	list_display = ['name']
	search_fields = ['name']


@admin.register(Comment)
class CommentShow(BaseModelAdmin):
	"""
	An admin model class for costuming comments on admin panel.
	"""
	search_fields = ['content']


@admin.register(Product)
class ProductShow(BaseModelAdmin):
	"""
	An admin model class for costuming products on admin panel.
	"""
	list_display = ['name', 'price']
	search_fields = ['name']


@admin.register(Discount)
class DiscountShow(admin.ModelAdmin):
	"""
	An admin model class for costuming discounts on admin panel.
	"""
	list_display = ['description', 'amount']
	search_fields = ['description']
	list_per_page = 15


@admin.register(Brand)
class BrandShow(BaseModelAdmin):
	"""
	An admin model class for costuming brands on admin panel.
	"""
	list_display = ['name']
	search_fields = ['name']
