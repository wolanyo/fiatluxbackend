# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0019_auto_20160612_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='downloadLink',
        ),
        migrations.RemoveField(
            model_name='document',
            name='mediaURL',
        ),
        migrations.AddField(
            model_name='book',
            name='excerptFile',
            field=models.FileField(verbose_name='Extrait', upload_to='books', null=True, default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(verbose_name='Fichier complet', upload_to='books', null=True, blank=True, default='link', max_length=500),
        ),
        migrations.AddField(
            model_name='cddvd',
            name='downloadLink',
            field=models.CharField(verbose_name='URL de telechargement', max_length=500, null=True, blank=True, default='link'),
        ),
        migrations.AddField(
            model_name='cddvd',
            name='mediaURL',
            field=models.CharField(verbose_name="URL de l'extrait", max_length=1000, null=True, default=''),
        ),
    ]
