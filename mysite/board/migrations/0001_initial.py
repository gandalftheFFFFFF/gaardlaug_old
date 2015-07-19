# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=200)),
                ('street_number', models.IntegerField()),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='boardmember',
            name='role',
            field=models.ForeignKey(to='board.Role', null=True),
        ),
    ]
