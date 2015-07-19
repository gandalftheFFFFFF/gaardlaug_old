# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='name',
        ),
        migrations.AddField(
            model_name='boardmember',
            name='first_name',
            field=models.CharField(default='placeholder first name', max_length=200),
        ),
        migrations.AddField(
            model_name='boardmember',
            name='last_name',
            field=models.CharField(default='placeholder last name', max_length=200),
        ),
    ]
