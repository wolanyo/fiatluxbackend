# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0021_auto_20160612_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cddvd',
            name='mediaURL',
            field=models.CharField(verbose_name="URL de l'extrait", max_length=1000, blank=True, default='', null=True),
        ),
    ]
