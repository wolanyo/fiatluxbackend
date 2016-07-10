# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0017_auto_20160612_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='section',
            field=models.CharField(default='SPIRITUALITY', verbose_name='Section', max_length=15, choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('SELF_DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')]),
        ),
    ]
