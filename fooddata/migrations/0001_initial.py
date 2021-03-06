# Generated by Django 3.2.9 on 2021-12-11 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(max_length=256)),
                ('kcal', models.IntegerField()),
                ('protein', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('sugars', models.FloatField()),
                ('fiber', models.FloatField()),
                ('total_fat', models.FloatField()),
                ('saturated_fat', models.FloatField()),
                ('monousaturated_fat', models.FloatField()),
                ('polyunsaturated_fat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('password', models.CharField(max_length=40, unique=True, validators=[django.core.validators.MinLengthValidator(8)])),
                ('date_of_birth', models.DateField(blank=True)),
                ('current_weight', models.FloatField(blank=True)),
                ('currently_logged_in', models.BooleanField()),
                ('date_account_created', models.DateField(auto_now_add=True)),
                ('last_logged_in', models.DateField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('email_address', models.EmailField(max_length=40)),
            ],
        ),
    ]
