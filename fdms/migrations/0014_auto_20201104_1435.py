# Generated by Django 3.0.8 on 2020-11-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdms', '0013_auto_20201104_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficary',
            name='beneficary',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='beneficary',
            name='benfcontact',
            field=models.EmailField(max_length=54),
        ),
    ]
