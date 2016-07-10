# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0003_auto_20160519_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiMediaArchive',
            fields=[
                ('common_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='webservices.Common')),
                ('mediaURL', models.CharField(default='', null=True, max_length=1000, verbose_name='URL de la ressosurce')),
                ('archiveType', models.CharField(blank=True, default='TVPROGRAM', choices=[('TVPROGRAM', 'TVPROGRAM'), ('SEMINARY', 'SEMINARY')], max_length=5, verbose_name='Média')),
                ('playerType', models.CharField(blank=True, default='YOUTUBE', choices=[('YOUTUBE', 'YOUTUBE'), ('DAILYMOTION', 'DAILYMOTION')], max_length=5, verbose_name='Player')),
                ('visibility', models.CharField(blank=True, default='FREE', choices=[('FREE', 'FREE'), ('NON_FREE', 'NON_FREE')], max_length=5, verbose_name='Visibility')),
            ],
            bases=('webservices.common',),
        ),
        migrations.RemoveField(
            model_name='tvprogram',
            name='common_ptr',
        ),
        migrations.DeleteModel(
            name='TvProgram',
        ),
    ]
