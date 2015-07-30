# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20150721_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploader',
            name='upload_date',
            field=models.DateTimeField(),
        ),
    ]
