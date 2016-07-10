# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0010_auto_20160529_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='common',
            name='section',
            field=models.CharField(blank=True, choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('SELF_DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')], default='SPIRITUALITY', verbose_name='Section', max_length=5),
        ),
        migrations.AlterField(
            model_name='common',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Image illustrative', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commonmedia',
            name='mediaType',
            field=models.CharField(blank=True, choices=[('TEXT', 'TEXT'), ('AUDIO', 'AUDIO'), ('VIDEO', 'VIDEO')], default='TEXT', verbose_name='Type de Média', max_length=5),
        ),
        migrations.AlterField(
            model_name='jokestoryreflect',
            name='type',
            field=models.CharField(verbose_name='Type', choices=[('BLAGUE', 'BLAGUE'), ('HISTOIRE', 'HISTOIRE'), ('PENSEE', 'PENSEE')], default='BLAGUE', max_length=10),
        ),
        migrations.AlterField(
            model_name='multimediaarchive',
            name='archiveType',
            field=models.CharField(blank=True, choices=[('TVPROGRAM', 'PROGRAMME TÉLÉ'), ('SEMINARY', 'SEMINAIRE')], default='TVPROGRAM', verbose_name='Type de Ressource', max_length=10),
        ),
        migrations.AlterField(
            model_name='multimediaarchive',
            name='playerType',
            field=models.CharField(blank=True, choices=[('YOUTUBE', 'YOUTUBE'), ('DAILYMOTION', 'DAILY MOTION')], default='YOUTUBE', verbose_name='Lecteur', max_length=10),
        ),
        migrations.AlterField(
            model_name='multimediaarchive',
            name='visibility',
            field=models.CharField(blank=True, choices=[('FREE', 'GRATUIT'), ('NON_FREE', 'NON GRATUIT')], default='FREE', verbose_name='Visibilité', max_length=10),
        ),
    ]
