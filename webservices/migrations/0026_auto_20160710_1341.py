# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0025_auto_20160710_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='excerpt',
            field=models.TextField(blank=True, max_length=2000, default='', null=True, verbose_name='Résumé'),
        ),
    ]
