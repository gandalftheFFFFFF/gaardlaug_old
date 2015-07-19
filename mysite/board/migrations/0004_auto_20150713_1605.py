# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20150713_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmember',
            name='from_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='role',
            field=models.ForeignKey(null=True, blank=True, to='board.Role'),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='street_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='to_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
