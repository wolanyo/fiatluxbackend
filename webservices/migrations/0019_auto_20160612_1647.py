# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0018_auto_20160612_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='image',
            field=models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Image illustrative'),
        ),
    ]
