# Generated by Django 4.0.6 on 2022-07-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DOB',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
