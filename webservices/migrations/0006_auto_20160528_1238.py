# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0005_jokestoryreflect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimediaarchive',
            name='archiveType',
            field=models.CharField(blank=True, max_length=10, choices=[('TVPROGRAM', 'TVPROGRAM'), ('SEMINARY', 'SEMINARY')], verbose_name='Média', default='TVPROGRAM'),
        ),
        migrations.AlterField(
            model_name='multimediaarchive',
            name='playerType',
            field=models.CharField(blank=True, max_length=10, choices=[('YOUTUBE', 'YOUTUBE'), ('DAILYMOTION', 'DAILYMOTION')], verbose_name='Player', default='YOUTUBE'),
        ),
        migrations.AlterField(
            model_name='multimediaarchive',
            name='visibility',
            field=models.CharField(blank=True, max_length=10, choices=[('FREE', 'FREE'), ('NON_FREE', 'NON_FREE')], verbose_name='Visibility', default='FREE'),
        ),
    ]
