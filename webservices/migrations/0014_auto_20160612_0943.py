# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0013_auto_20160612_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='gender',
        ),
        migrations.AlterField(
            model_name='donate',
            name='civility',
            field=models.CharField(null=True, max_length=100, verbose_name='Civilité', choices=[('M', 'M'), ('Mlle', 'Mlle'), ('Mme', 'Mme')], blank=True, default='Mlle'),
        ),
        migrations.AlterField(
            model_name='donate',
            name='dateDonate',
            field=models.DateField(verbose_name='Date du don'),
        ),
    ]
