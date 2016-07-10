# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0004_auto_20160528_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='JokeStoryReflect',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, to='webservices.Common', parent_link=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=5, default='BLAGUE', choices=[('BLAGUE', 'BLAGUE'), ('HISTOIRE', 'HISTOIRE'), ('PENSÉ', 'PENSÉ')])),
                ('content', models.TextField(verbose_name='Contenu')),
            ],
            options={
                'verbose_name_plural': 'Blagues, Histoires, Pensés',
                'verbose_name': 'Blague, Histoire, Pensé',
            },
            bases=('webservices.common',),
        ),
    ]
