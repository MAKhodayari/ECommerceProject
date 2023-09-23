from core.tasks import *
from core.utils import queryset_id_name


def delete_action(modeladmin, request, queryset):
	object_ids, model_name = queryset_id_name(queryset)
	delete_task.delay(model_name, object_ids)


def undelete_action(modeladmin, request, queryset):
	object_ids, model_name = queryset_id_name(queryset)
	undelete_task.delay(model_name, object_ids)


def activate_action(modeladmin, request, queryset):
	object_ids, model_name = queryset_id_name(queryset)
	activate_task.delay(model_name, object_ids)


def deactivate_action(modeladmin, request, queryset):
	object_ids, model_name = queryset_id_name(queryset)
	deactivate_task.delay(model_name, object_ids)


delete_action.short_description = 'Delete Selected'
undelete_action.short_description = 'Undelete Selected'
activate_action.short_description = 'Activate Selected'
deactivate_action.short_description = 'Deactivate Selected'
