# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_image'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploader',
            name='post',
            field=models.ForeignKey(null=True, blank=True, to='blog.Post'),
        ),
    ]
