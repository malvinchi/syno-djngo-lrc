# Generated by Django 3.0.8 on 2020-11-22 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fdms', '0014_auto_20201104_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficary',
            name='beneficary',
        ),
        migrations.AddField(
            model_name='beneficary',
            name='benef',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beneficary',
            name='benfcontact',
            field=models.EmailField(max_length=54, unique=True),
        ),
    ]
