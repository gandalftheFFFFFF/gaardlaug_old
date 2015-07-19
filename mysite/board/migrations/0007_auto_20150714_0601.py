# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20150714_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmember',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='first_name',
            field=models.CharField(max_length=200, default='first name'),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='from_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='last_name',
            field=models.CharField(max_length=200, default='last name'),
        ),
    ]
