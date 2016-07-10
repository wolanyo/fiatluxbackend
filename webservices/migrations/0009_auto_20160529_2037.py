# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0008_auto_20160528_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='cddvd',
            name='mediaURL',
            field=models.CharField(default='', max_length=1000, verbose_name="URL de l'extrait", null=True),
        ),
        migrations.AlterField(
            model_name='jokestoryreflect',
            name='type',
            field=models.CharField(default='BLAGUE', max_length=10, choices=[('BLAGUE', 'BLAGUE'), ('HISTOIRE', 'HISTOIRE'), ('PENSEE', 'PENSEE')]),
        ),
    ]
