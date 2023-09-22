from django.db import models

from core.models import BaseDiscount, BaseModel
from customer.models import Customer, Address
from product.models import Product


class Coupon(BaseDiscount):
	"""
	The coupon(of-code) model.
	"""
	code = models.CharField(max_length=50, help_text='Coupon Code', unique=True)

	# Remove unnecessary verbose names

	def __str__(self):
		return f"Coupon type:{self.type} Amount{self.amount} Code{self.code}"

	def discounted_price(self, price: int) -> int:
		"""
		Calculates the price after using coupon
		:param price: product price
		:return: discounted price
		"""
		if self.type == 'val':
			if price < self.amount:
				# More discount than price
				return price
			return price - self.amount
		elif self.type == "cent":
			return price - int((self.amount / 100) * price)


class Status(BaseModel):
	"""
	The status model.
	"""
	STATUS_CHOICES = [
		('new', 'New'),
		('check', 'Check Out'),
		('paid', 'Paid'),
		('failed', 'Failed')
	]
	title = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new', help_text='Status Options')

	class Meta:
		# Remove unnecessary verbose name
		verbose_name_plural = 'Status'

	def __str__(self):
		return f"Status: {self.title} Code: {self.pk}"


class Order(BaseModel):
	"""
	The order model.
	"""
	status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
	customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
	coupon = models.OneToOneField(to=Coupon, on_delete=models.PROTECT, null=True, blank=True)
	total_price = models.PositiveIntegerField(default=0, help_text='Total price of the order')
	final_price = models.PositiveIntegerField(default=0, help_text='Final price after using coupon code')
	address = models.ForeignKey(to=Address, on_delete=models.PROTECT, null=True, blank=True)

	# Remove unnecessary verbose names

	def __str__(self):
		return f"Order for customer: {self.customer} Status: {self.status}"


class OrderItem(BaseModel):
	"""
	The order item model.
	"""
	product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
	order = models.ForeignKey(to=Order, on_delete=models.PROTECT)
	count = models.PositiveIntegerField(default=1, help_text='Count of order items')

	# Remove unnecessary verbose names

	def __str__(self):
		return f"Product: {self.product} X{self.count}"

	@property
	def total(self):
		"""
		Calculation of total order items price
		:return:
		"""
		return int(self.product.calc_discounted) * int(self.count)
