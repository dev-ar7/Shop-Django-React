# Generated by Django 4.0.5 on 2022-06-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(max_length=25, unique=True)),
                ('image', models.ImageField(upload_to='product_pics')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('qty', models.PositiveSmallIntegerField(default=1, help_text='Quantity')),
                ('inventory', models.PositiveSmallIntegerField()),
                ('description', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('two', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('three', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('four', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('five', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='store.product')),
            ],
            options={
                'ordering': ['product'],
            },
        ),
    ]