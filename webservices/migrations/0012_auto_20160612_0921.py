# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0011_auto_20160612_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='section',
            field=models.CharField(verbose_name='Section', max_length=5, default='SPIRITUALITY', choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('SELF_DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')]),
        ),
    ]
