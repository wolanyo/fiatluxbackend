# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0020_auto_20160612_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='excerptFile',
            field=models.FileField(verbose_name='Extrait', null=True, upload_to='books', default='', blank=True),
        ),
    ]
