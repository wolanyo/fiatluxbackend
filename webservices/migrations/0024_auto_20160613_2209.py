# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0023_lessontype_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='section',
            field=models.CharField(choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('SELF_DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')], verbose_name='Section', max_length=30, default='SPIRITUALITY'),
        ),
        migrations.AlterField(
            model_name='lessontype',
            name='section',
            field=models.CharField(choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('SELF_DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')], verbose_name='Section', max_length=30, default='SPIRITUALITY'),
        ),
    ]
