# Generated by Django 4.0.6 on 2022-07-22 14:12

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0003_remove_address_last_login_remove_address_password_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='employeeuserauth',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
