from django.contrib import admin

# Better import
from product.models import *


# Register first
@admin.register(Category)
class CategoryShow(admin.ModelAdmin):
	"""
	An admin model class for costuming categories on admin panel.
	"""
	list_display = ['name']
	search_fields = ['name']
	list_per_page = 15


@admin.register(Comment)
class CommentShow(admin.ModelAdmin):
	"""
	An admin model class for costuming comments on admin panel.
	"""
	search_fields = ['content']
	list_per_page = 15


@admin.register(Product)
class ProductShow(admin.ModelAdmin):
	"""
	An admin model class for costuming products on admin panel.
	"""
	list_display = ['name', 'price']
	search_fields = ['name']
	list_per_page = 15


@admin.register(Discount)
class DiscountShow(admin.ModelAdmin):
	"""
	An admin model class for costuming discounts on admin panel.
	"""
	list_display = ['description', 'amount']
	search_fields = ['description']
	list_per_page = 15


@admin.register(Brand)
class BrandShow(admin.ModelAdmin):
	"""
	An admin model class for costuming brands on admin panel.
	"""
	list_display = ['name']
	search_fields = ['name']
	list_per_page = 15
