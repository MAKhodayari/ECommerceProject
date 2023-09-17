# Generated by Django 4.0.2 on 2023-04-27 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
	initial = True

	dependencies = [
		('customer', '0001_initial'),
		('product', '__first__'),
	]

	operations = [
		migrations.CreateModel(
			name='Coupon',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('amount', models.PositiveIntegerField(default=0)),
				('description', models.CharField(max_length=70)),
				('type', models.CharField(choices=[('cent', 'percent'), ('val', 'value')], max_length=5)),
				('code', models.CharField(help_text='Coupon Code', max_length=50, unique=True)),
			],
			options={
				'verbose_name': 'Coupon',
				'verbose_name_plural': 'Coupons',
			},
		),
		migrations.CreateModel(
			name='Order',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('total_price', models.PositiveIntegerField(default=0, help_text='Total price of the order')),
				(
				'final_price', models.PositiveIntegerField(default=0, help_text='Final price after using coupon code')),
				('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
											  to='customer.address')),
				('coupon', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
												to='order.coupon')),
				('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
			],
			options={
				'verbose_name': 'Order',
				'verbose_name_plural': 'Orders',
			},
		),
		migrations.CreateModel(
			name='Status',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('title', models.CharField(
					choices=[('new', 'New'), ('check', 'Check Out'), ('paid', 'Paid'), ('failed', 'Failed')],
					default='new', help_text='Status Options', max_length=10)),
			],
			options={
				'verbose_name': 'Status',
				'verbose_name_plural': 'Status',
			},
		),
		migrations.CreateModel(
			name='OrderItem',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('count', models.PositiveIntegerField(default=1, help_text='Count of order items')),
				('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order')),
				('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
			],
			options={
				'verbose_name': 'OrderItem',
				'verbose_name_plural': 'OrderItems',
			},
		),
		migrations.AddField(
			model_name='order',
			name='status',
			field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.status'),
		),
	]
