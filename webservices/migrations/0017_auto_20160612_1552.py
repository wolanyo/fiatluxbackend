# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0016_auto_20160612_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='image',
            field=models.ImageField(blank=True, verbose_name='Image illustrative', upload_to='', null=True),
        ),
    ]
