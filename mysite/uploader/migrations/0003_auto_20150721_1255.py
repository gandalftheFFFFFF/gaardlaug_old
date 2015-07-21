# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_uploader_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploader',
            name='category',
            field=models.CharField(max_length=200, choices=[('regnskab', 'Regnskab'), ('referat', 'Referat'), ('andet', 'Andet')], default='media'),
        ),
    ]
