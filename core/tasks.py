from core.utils import get_selected_objects
from ecommerce.celery import app


@app.task
def delete_task(model_name, object_ids):
	objs = get_selected_objects(model_name, object_ids)
	for obj in objs:
		obj.delete()


@app.task
def undelete_task(model_name, object_ids):
	objs = get_selected_objects(model_name, object_ids)
	for obj in objs:
		obj.undelete()


@app.task
def activate_task(model_name, object_ids):
	objs = get_selected_objects(model_name, object_ids)
	for obj in objs:
		obj.activate()


@app.task
def deactivate_task(model_name, object_ids):
	objs = get_selected_objects(model_name, object_ids)
	for obj in objs:
		obj.deactivate()
