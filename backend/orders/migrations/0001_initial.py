# Generated by Django 4.0.5 on 2022-06-09 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.JSONField(null=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator('\\d{3}?-?\\d{3}?-?\\d{4}', 'Only numbers allowed.')])),
                ('address', models.CharField(max_length=221)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
                ('subtotal', models.CharField(max_length=10)),
                ('tax', models.CharField(max_length=10, null=True)),
                ('total', models.CharField(max_length=10, null=True)),
                ('status', models.CharField(choices=[('PND', 'Pending'), ('RTN', 'Return'), ('CMPL', 'Completed')], default='PND', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['status', 'created_at'],
            },
        ),
    ]
