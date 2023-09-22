import json

from django.db.models import Sum

from order.models import Order, OrderItem


def cart_number(request):
	"""
	A context manager for the number in navbar shopping cart
	:param request:
	:return: A number to be place in navbar
	"""
	if request.user.is_authenticated:
		try:
			# Use get for just one object
			order = Order.objects.get(customer__user=request.user, status_id=1)
		# Add exception handler
		except Order.DoesNotExist:
			return {'number': 0}
		else:
			# Use aggregation to return cart number
			order_item = OrderItem.objects.filter(order=order).aggregate(Sum('count'))
			if order_item['count__sum'] is None:
				return {'number': 0}
			return {'number': order_item['count__sum']}
	else:
		cookie = request.COOKIES.get('product')
		try:
			jsoned = json.loads(cookie)
		# Add exception handler
		except json.JSONDecodeError:
			return {'number': 0}
		else:
			# Use sum to get number of cart items
			number = sum(jsoned.values())
			print(number)
			return {'number': number}
