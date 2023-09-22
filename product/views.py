from django.views import generic
from rest_framework import generics

from product.models import Product, Category, Brand
from product.serializers import ProductSerializer


class ProductViewList(generic.ListView):
	"""
	A view to show the product list and categories for shop section.
	"""
	queryset = Category.objects.filter(is_active=True, is_delete=False).order_by('name')[:5]
	template_name = 'product/product_list.html'
	extra_context = {'title': 'Products'}

	def get_context_data(self, *, object_list=None, **kwargs):
		kwargs['product'] = Product.objects.all()
		kwargs['brand'] = Brand.objects.all()
		return super().get_context_data(object_list=object_list, **kwargs)


class ProductListAPI(generics.ListCreateAPIView):
	"""
	API view to filter the products.
	"""
	serializer_class = ProductSerializer
	queryset = Product.objects.filter()

	def get_queryset(self):
		# Rename to filter for better readability
		filters = dict(self.request.GET)
		for k, v in filters.items():
			filters[k] = ''.join(v)
		try:
			queryset = Product.objects.filter(**filters)
		# Add exception handler
		except Product.DoesNotExist:
			return super().get_queryset()
		return queryset


class ProductViewDetail(generic.DetailView):
	"""
	The detail view for each product.
	"""
	model = Product
	template_name = 'product/product_detail.html'
