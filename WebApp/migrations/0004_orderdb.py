# Generated by Django 5.1 on 2024-11-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('DishName', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('TotalAmount', models.IntegerField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]