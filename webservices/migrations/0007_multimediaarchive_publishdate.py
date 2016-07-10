# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0006_auto_20160528_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimediaarchive',
            name='publishDate',
            field=models.DateField(default=datetime.datetime(2016, 5, 28, 12, 46, 10, 230141, tzinfo=utc), auto_now_add=True, verbose_name='Date de publication'),
            preserve_default=False,
        ),
    ]
