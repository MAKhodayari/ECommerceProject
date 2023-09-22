from django.contrib import admin

# Better import
from order.models import *

admin.site.register([OrderItem, Order, Status, Coupon])
