from django.urls import path

from landing.views import IndexView, ContactView

app_name = 'landing'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('contact/', ContactView.as_view(), name='contact'),
]
