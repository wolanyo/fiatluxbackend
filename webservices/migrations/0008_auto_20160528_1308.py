# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0007_multimediaarchive_publishdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokestoryreflect',
            name='type',
            field=models.CharField(max_length=10, choices=[('BLAGUE', 'BLAGUE'), ('HISTOIRE', 'HISTOIRE'), ('PENSÉ', 'PENSÉ')], default='BLAGUE'),
        ),
    ]
