from django.urls import path

from product.views import ProductViewList, ProductListAPI, ProductViewDetail

urlpatterns = [
	path('', ProductViewList.as_view(), name='product_list'),
	path('<int:pk>/', ProductViewDetail.as_view(), name='product_detail'),
	path('api/', ProductListAPI.as_view(), name='product_list_api'),
]
