# Generated by Django 3.2.9 on 2021-11-29 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 8, 30, 21, 373283), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 8, 30, 21, 373283)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 8, 30, 21, 375277)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 8, 30, 21, 371264)),
        ),
    ]
