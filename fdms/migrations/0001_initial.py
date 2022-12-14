# Generated by Django 3.0.8 on 2020-10-08 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficary', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instname', models.CharField(choices=[('CB', 'Canara Bank'), ('DB', 'DhanBank'), ('FB', 'FedBank')], max_length=20, verbose_name='Name of Institution')),
                ('instype', models.CharField(choices=[('BNK', 'Bank'), ('FNC', 'FinanceCompany'), ('INS', 'InsuranceComp')], max_length=20, verbose_name='Type of Intstitute')),
            ],
        ),
        migrations.CreateModel(
            name='Securities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectype', models.CharField(choices=[('FD', 'Fd'), ('MIS', 'Mis'), ('SIP', 'Sip'), ('INSR', 'Insr')], max_length=20, verbose_name='Security Type')),
                ('status', models.BooleanField(default='open')),
                ('doc', models.DateField(verbose_name='Date of Commencement')),
                ('tenure', models.IntegerField(default=1, max_length=2)),
                ('roi', models.IntegerField(default=5, max_length=2, verbose_name='rate of int')),
                ('dd', models.DateField(verbose_name='due date')),
                ('nob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdms.Beneficaries')),
                ('noi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdms.Institutions')),
            ],
        ),
    ]
