# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150713_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmember',
            name='from_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 16, 2, 56, 60161, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='street_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 16, 3, 5, 803309, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
