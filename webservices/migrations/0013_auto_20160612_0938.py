# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0012_auto_20160612_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
