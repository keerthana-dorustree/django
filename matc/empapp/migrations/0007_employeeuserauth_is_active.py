# Generated by Django 4.0.6 on 2022-07-25 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0006_alter_employeeuserauth_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeuserauth',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
