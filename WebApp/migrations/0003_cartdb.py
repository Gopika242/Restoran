# Generated by Django 5.1 on 2024-11-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_signupdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('DishName', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
