# Generated by Django 5.1.1 on 2024-10-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('pass1', models.CharField(blank=True, max_length=100, null=True)),
                ('re_pass', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
