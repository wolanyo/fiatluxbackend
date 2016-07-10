# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0009_auto_20160529_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cddvd',
            name='mediaURL',
        ),
        migrations.AddField(
            model_name='document',
            name='mediaURL',
            field=models.CharField(null=True, max_length=1000, verbose_name="URL de l'extrait", default=''),
        ),
    ]
