# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0024_auto_20160613_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('common_ptr', models.OneToOneField(primary_key=True, to='webservices.Common', auto_created=True, serialize=False, parent_link=True)),
                ('author', models.CharField(verbose_name='Auteur', default='', max_length=200)),
                ('publicationDate', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Aidons-nous',
                'verbose_name_plural': 'Aidons-nous',
            },
            bases=('webservices.common',),
        ),
        migrations.CreateModel(
            name='Publicity',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(primary_key=True, to='webservices.CommonMedia', auto_created=True, serialize=False, parent_link=True)),
                ('publicationDate', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Publicité',
                'verbose_name_plural': 'Publicités',
            },
            bases=('webservices.commonmedia',),
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('common_ptr', models.OneToOneField(primary_key=True, to='webservices.Common', auto_created=True, serialize=False, parent_link=True)),
                ('eventDate', models.DateField(verbose_name='Date')),
                ('startTime', models.TimeField(verbose_name='Heure de début')),
                ('endTime', models.TimeField(verbose_name='Heure de fin')),
                ('address', models.CharField(verbose_name='Adresse', default='Siège du PARAM AKSHAR', max_length=500)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
            bases=('webservices.common',),
        ),
        migrations.AlterField(
            model_name='common',
            name='section',
            field=models.CharField(verbose_name='Section', choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')], default='SPIRITUALITY', max_length=30),
        ),
        migrations.AlterField(
            model_name='lessontype',
            name='position',
            field=models.IntegerField(verbose_name='Position', null=True, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='lessontype',
            name='section',
            field=models.CharField(verbose_name='Section', choices=[('SPIRITUALITY', 'SPIRITUALITÉ'), ('DEVELOPMENT', 'DEVELOPPEMENT PERSONNNEL')], default='SPIRITUALITY', max_length=30),
        ),
        migrations.AlterField(
            model_name='multimediaarchive',
            name='archiveType',
            field=models.CharField(max_length=10, verbose_name='Type de Ressource', choices=[('TVPROGRAM', 'PROGRAMME TÉLÉ'), ('SEMINARY', 'SEMINAIRE'), ('MUSIC', 'MUSIQUE')], default='TVPROGRAM', blank=True),
        ),
    ]
