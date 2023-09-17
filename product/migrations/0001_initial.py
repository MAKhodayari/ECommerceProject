# Generated by Django 4.0.2 on 2023-04-27 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Brand',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('name', models.CharField(default='', help_text='Name of brand', max_length=50)),
			],
			options={
				'verbose_name': 'Brand',
				'verbose_name_plural': 'Brands',
			},
		),
		migrations.CreateModel(
			name='Category',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('name', models.CharField(default='', help_text='Name of Category', max_length=50)),
				('image', models.FileField(blank=True, default=None, null=True, upload_to='category/')),
			],
			options={
				'verbose_name': 'Category',
				'verbose_name_plural': 'Categories',
			},
		),
		migrations.CreateModel(
			name='Comment',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('content',
				 models.CharField(default='So far so good', help_text='Comment text', max_length=250, null=True)),
			],
			options={
				'verbose_name': 'Comment',
				'verbose_name_plural': 'Comments',
			},
		),
		migrations.CreateModel(
			name='Discount',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('amount', models.PositiveIntegerField(default=0)),
				('description', models.CharField(max_length=70)),
				('type', models.CharField(choices=[('cent', 'percent'), ('val', 'value')], max_length=5)),
			],
			options={
				'verbose_name': 'Discount',
				'verbose_name_plural': 'Discounts',
			},
		),
		migrations.CreateModel(
			name='Product',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('create_datetime', models.DateTimeField(auto_now_add=True)),
				('modify_datetime', models.DateTimeField(auto_now=True)),
				('is_active', models.BooleanField(default=True, editable=False)),
				('is_delete', models.BooleanField(default=False, editable=False)),
				('name', models.CharField(default='', help_text='Name of product', max_length=50)),
				('image', models.FileField(blank=True, default=None, null=True, upload_to='product/')),
				('price', models.PositiveIntegerField(default=0, help_text='Price of product')),
				('description',
				 models.CharField(default='description', help_text='Product description', max_length=250)),
				('count', models.PositiveIntegerField(default=1, help_text='Count of product')),
				('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.brand')),
				('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
				('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
											  to='product.comment')),
				('discount', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
												  to='product.discount')),
			],
			options={
				'verbose_name': 'Product',
				'verbose_name_plural': 'Products',
			},
		),
		migrations.AddField(
			model_name='category',
			name='discount',
			field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
									   to='product.discount'),
		),
		migrations.AddField(
			model_name='category',
			name='parent',
			field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
									to='product.category', verbose_name='Parent Category'),
		),
		migrations.AddField(
			model_name='brand',
			name='discount',
			field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
									   to='product.discount'),
		),
	]
