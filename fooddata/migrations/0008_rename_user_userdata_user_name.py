# Generated by Django 3.2.9 on 2021-12-13 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooddata', '0007_auto_20211212_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='user',
            new_name='user_name',
        ),
    ]
