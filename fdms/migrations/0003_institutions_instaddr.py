# Generated by Django 3.0.8 on 2020-10-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdms', '0002_auto_20201009_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutions',
            name='instaddr',
            field=models.CharField(default='india', help_text='Enter City Name', max_length=100, verbose_name='Institution Address'),
        ),
    ]
