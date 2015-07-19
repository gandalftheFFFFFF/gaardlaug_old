# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20150714_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cadsatre_name', models.CharField(max_length=200)),
            ],
        ),
    ]
