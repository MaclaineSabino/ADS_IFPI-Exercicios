# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_itemvenda_codigovenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='CodigoFornecedor',
            field=models.CharField(max_length=20),
        ),
    ]
