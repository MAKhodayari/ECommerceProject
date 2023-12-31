from django.contrib import admin

# Remove unused imports
from core.actions import *
from core.models import User


class BaseModelAdmin(admin.ModelAdmin):
	actions = [delete_action, undelete_action, activate_action, deactivate_action]
	list_per_page = 15


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	"""
	Customizing users on admin panel.
	"""
	list_display = ['username', 'first_name', 'last_name', ]
	search_fields = ['username', 'first_name', 'last_name', ]
	list_per_page = 15
