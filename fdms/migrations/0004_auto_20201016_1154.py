# Generated by Django 3.0.8 on 2020-10-16 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdms', '0003_institutions_instaddr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Beneficaries',
            new_name='Beneficary',
        ),
        migrations.RenameField(
            model_name='securities',
            old_name='nob',
            new_name='beneficary',
        ),
        migrations.RenameField(
            model_name='securities',
            old_name='noi',
            new_name='institution',
        ),
    ]
