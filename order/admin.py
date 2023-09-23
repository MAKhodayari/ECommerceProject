from django.contrib import admin

# Better import
from core.admin import BaseModelAdmin
from order.models import *


@admin.register(Order)
class OrderAdmin(BaseModelAdmin):
	...


@admin.register(OrderItem)
class OrderItemAdmin(BaseModelAdmin):
	...


@admin.register(Status)
class StatusAdmin(BaseModelAdmin):
	...


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
	...
