# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0015_donate_paymenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='civility',
            field=models.CharField(null=True, choices=[('M', 'M'), ('Mlle', 'Mlle'), ('Mme', 'Mme')], default='Mlle', blank=True, max_length=10, verbose_name='Civilité'),
        ),
        migrations.AlterField(
            model_name='donate',
            name='paymentType',
            field=models.CharField(null=True, choices=[('FLOOZ', 'FLOOZ'), ('TOGOCELL', 'TOGOCELL'), ('CHRONOCASH', 'CHRONOCASH'), ('CARD', 'VISA / MASTERCARD / CARTE BLEU'), ('PAYPAL', 'PAYPAL')], default='FLOOZ', blank=True, max_length=50, verbose_name='Type de Paiement'),
        ),
    ]
