from rest_framework import permissions


class IsOwner(permissions.BasePermission):
	"""
	Using Django permissions to check if the user is owner or not
	"""
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return obj.user == request.user
		return False


class IsSuperUser(permissions.BasePermission):
	"""
	Using Django permissions to check if the user is superuser or not
	"""
	def has_permission(self, request, view):
		# Simplify return statement
		return request.user and request.user.is_superuser
