from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, RedirectView, TemplateView, ListView
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.utils import cookie_to_database
from customer.forms import CustomerSignupForm
from customer.models import Customer, Address
from customer.serializers import AddressSerializer, CustomerSerializer
from order.models import Order


class OrderView(LoginRequiredMixin, ListView):
	"""
	A view for filtering and sending history of the customer orders.
	"""
	model = Order
	context_object_name = 'items'

	def get(self, request, *args, **kwargs):
		"""
		Overriding get method for filtering paid customer orders
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		order = Order.objects.filter(customer__user=self.request.user, status_id=2)
		context = {'items': order}
		template_str = render_to_string(template_name='customer/order_history.html', context=context)
		return JsonResponse({'order': template_str})


class AddressView(LoginRequiredMixin, ListView):
	"""
	A view for filtering and sending addresses to customer panel.
	"""
	model = Address
	context_object_name = 'items'

	def get(self, request, *args, **kwargs):
		"""
		Overriding get method for filtering customer addresses.
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		address = Address.objects.filter(customer__user=self.request.user)
		context = {'items': address}
		template_str = render_to_string(template_name='customer/address_list.html', context=context)
		return JsonResponse({'address': template_str})


class CustomerLoginView(FormView):
	"""
	A view for customer login
	"""
	form_class = AuthenticationForm
	template_name = "customer/reg_login.html"
	success_url = reverse_lazy('landing:index')
	# Remove unnecessary success_message

	# Remove unchanged form_invalid function

	def form_valid(self, form):
		"""
		Overriding this method, so it will get/create a customer, log the user in and sends data from cookie to database
		if form is valid.
		:param form:
		:return:
		"""
		login(self.request, user=form.get_user())
		user = self.request.user
		Customer.objects.get_or_create(user=user)
		if self.request.COOKIES.get('product'):
			cookie_to_database(self.request)
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		"""
		Overriding this method to send customer signup and login forms to template.
		:param kwargs:
		:return:
		"""
		# Change duplicate login_form
		kwargs['login_form'] = self.get_form()
		kwargs['signup_form'] = CustomerSignupForm()
		return super().get_context_data(**kwargs)


class CustomerSignupView(FormView):
	"""
	A view for customer signup
	"""
	form_class = CustomerSignupForm
	template_name = 'customer/reg_login.html'
	success_url = reverse_lazy('landing:index')

	def form_valid(self, form):
		"""
		Overriding this method to create a django user and saves into database if form is valid.
		:param form:
		:return:
		"""
		# Login user after registration
		user = form.save()
		login(self.request, user)
		return super().form_valid(form)

	def form_invalid(self, form):
		"""
		Overriding this method so if the user exists and is inactive it will activate the user and calls form valid.
		:param form:
		:return:
		"""
		phone = form.data.get('phone', )
		same_user = User.objects.filter(phone=phone, is_active=False)
		if same_user and form.data.get('password1', ) == form.data.get('password2', ) and form.data.get(
				'password1', ) is not None:
			same_user: User
			same_user.is_active = True
			return super().form_valid(form)
		return super().form_invalid(form)

	def get_context_data(self, **kwargs):
		"""
		Overriding this method to send customer signup and login forms to template.
		:param kwargs:
		:return:
		"""
		kwargs['login_form'] = AuthenticationForm()
		# Change duplicate login_form
		kwargs['signup_form'] = self.get_form()
		return super().get_context_data(**kwargs)


class LogoutView(LoginRequiredMixin, RedirectView):
	"""
	Provides users the ability to logout
	"""
	url = reverse_lazy('landing:index')

	def get(self, request, *args, **kwargs):
		"""
		Overriding this method to logout the user.
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		logout(request)
		return super(LogoutView, self).get(request, *args, **kwargs)


class PanelView(LoginRequiredMixin, TemplateView):
	"""
	A simple template view for rendering the html file for the customer panel.
	"""
	template_name = 'customer/panel.html'


class AddAddressesView(LoginRequiredMixin, CreateAPIView):
	"""
	A view for adding new addresses into customer
	"""
	serializer_class = AddressSerializer
	queryset = Address.objects.all()

	def create(self, request, *args, **kwargs):
		"""
		Overriding this method to create new addresses.
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		request.data._mutable = True
		customer = Customer.objects.get(user=self.request.user)
		request.data['customer'] = customer.id
		return super().create(request, *args, **kwargs)


class DeleteAddressesView(LoginRequiredMixin, DestroyAPIView):
	"""
	A view for deleting the customer addresses.
	"""
	serializer_class = AddressSerializer
	queryset = Address.objects.all()


# Add view set for addresses
class AddressViewSet(LoginRequiredMixin, ModelViewSet):
	serializer_class = AddressSerializer
	queryset = Address.objects.all()

	def create(self, request, *args, **kwargs):
		request.data._mutable = True
		customer = Customer.objects.get(user=self.request.user)
		request.data['customer'] = customer.id
		return super().create(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, ListView):
	"""
	A view for showing the customer brief information.
	"""
	queryset = Customer.objects.all()
	context_object_name = 'items'

	def get(self, request, *args, **kwargs):
		"""
		Overriding this method to show the customer information.
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		# Use get to access customer
		customer = Customer.objects.get(user=self.request.user)
		context = {'items': customer}
		template_str = render_to_string(template_name='customer/profile.html', context=context)
		return JsonResponse({'customer': template_str})


class UpdateProfileView(LoginRequiredMixin, UpdateAPIView):
	"""
	A view for editing customer information.
	"""
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()


class Dashboard(LoginRequiredMixin, ListView):
	"""
	A view for customer brief information.
	"""
	queryset = Order.objects.all()

	def get(self, request, *args, **kwargs):
		# Use get to access customer
		customer = Customer.objects.get(user=self.request.user)
		context = {'items': customer}
		template_str = render_to_string(template_name='customer/dashboard.html', context=context)
		return JsonResponse({'customer': template_str})


class PasswordChange(LoginRequiredMixin, FormView):
	"""
	A view for customer changing his password.
	"""
	form_class = PasswordChangeForm
	template_name = 'customer/password.html'
	success_url = reverse_lazy('landing:index')

	def get(self, request, *args, **kwargs):
		customer = PasswordChangeForm(user=self.request.user)
		context = {'items': customer}
		template_str = render_to_string(template_name='customer/password.html', context=context)
		return JsonResponse({'password': template_str})

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def form_valid(self, form):
		# Remove prints
		messages.success(self.request, 'Done!!!!')
		form.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		# Remove prints
		# Use message error instead of message success
		messages.error(self.request, 'Error!!!!')
		return super().form_invalid(form)
