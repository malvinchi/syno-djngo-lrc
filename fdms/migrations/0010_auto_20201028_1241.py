# Generated by Django 3.0.8 on 2020-10-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdms', '0009_auto_20201020_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficary',
            name='beneficary',
            field=models.CharField(max_length=30),
        ),
    ]
