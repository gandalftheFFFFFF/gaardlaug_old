# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uploader.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('file_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='documents', choices=[('regnskab', 'Regnskab'), ('referat', 'Referat'), ('andet', 'Andet')], max_length=200)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('doc', models.FileField(upload_to=uploader.models.get_upload_path)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
