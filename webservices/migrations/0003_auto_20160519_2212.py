# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0002_auto_20160515_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reflect',
            fields=[
                ('common_ptr', models.OneToOneField(to='webservices.Common', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
            ],
            options={
                'verbose_name': 'Graine à méditer',
                'verbose_name_plural': 'Graines à méditer',
            },
            bases=('webservices.common',),
        ),
        migrations.CreateModel(
            name='TvProgram',
            fields=[
                ('common_ptr', models.OneToOneField(to='webservices.Common', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('mediaURL', models.CharField(verbose_name='URL de la ressosurce', blank=True, null=True, max_length=1000, default='')),
            ],
            options={
                'verbose_name': 'Emission télé',
                'verbose_name_plural': 'Emissions télé',
            },
            bases=('webservices.common',),
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Livre', 'verbose_name_plural': 'Livres'},
        ),
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name': 'Chapitre de leçon', 'verbose_name_plural': 'Chapitres des leçons'},
        ),
        migrations.AlterModelOptions(
            name='joke',
            options={'verbose_name': 'Blague', 'verbose_name_plural': 'Blagues'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Leçon', 'verbose_name_plural': 'Leçons'},
        ),
        migrations.AlterModelOptions(
            name='lessontype',
            options={'verbose_name': 'Type de leçon', 'verbose_name_plural': 'Types de leçons'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='strangestorie',
            options={'verbose_name': 'Histoire Etrange', 'verbose_name_plural': 'Histoires Etranges'},
        ),
        migrations.AddField(
            model_name='post',
            name='mediaURL',
            field=models.CharField(verbose_name='URL de la ressosurce', blank=True, null=True, max_length=1000, default=''),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='position',
            field=models.IntegerField(verbose_name='Position', default=0),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='position',
            field=models.IntegerField(verbose_name='Position', default=0),
        ),
        migrations.AlterField(
            model_name='lessontype',
            name='position',
            field=models.IntegerField(verbose_name='Position', blank=True, null=True, max_length=100, default=0),
        ),
    ]
