# Generated by Django 4.0.6 on 2022-07-22 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_alter_person_dob_alter_person_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='address',
            name='password',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='person',
            name='password',
        ),
    ]