# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0014_auto_20160612_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='paymentType',
            field=models.CharField(null=True, default='FLOOZ', max_length=100, verbose_name='Type de Paiement', blank=True, choices=[('FLOOZ', 'FLOOZ'), ('TOGOCELL', 'TOGOCELL'), ('CHRONOCASH', 'CHRONOCASH'), ('CARD', 'VISA / MASTERCARD / CARTE BLEU'), ('PAYPAL', 'PAYPAL')]),
        ),
    ]
