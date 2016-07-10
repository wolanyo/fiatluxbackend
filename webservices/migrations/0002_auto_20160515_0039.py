# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='position',
            field=models.IntegerField(unique=True, verbose_name='Position', default=0),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='position',
            field=models.IntegerField(unique=True, verbose_name='Position', default=0),
        ),
        migrations.AlterField(
            model_name='lessontype',
            name='position',
            field=models.IntegerField(default=0, unique=True, verbose_name='Position', blank=True, max_length=100, null=True),
        ),
    ]
