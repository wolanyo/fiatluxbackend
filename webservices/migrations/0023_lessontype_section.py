# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0022_auto_20160612_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessontype',
            name='section',
            field=models.CharField(verbose_name='Section', choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('SELF_DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')], default='SPIRITUALITY', max_length=15),
        ),
    ]
