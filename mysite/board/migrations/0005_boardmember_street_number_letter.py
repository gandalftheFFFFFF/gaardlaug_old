# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20150713_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmember',
            name='street_number_letter',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
