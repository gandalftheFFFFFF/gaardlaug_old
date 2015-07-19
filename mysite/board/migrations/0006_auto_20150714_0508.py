# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_boardmember_street_number_letter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='role',
        ),
        migrations.AddField(
            model_name='role',
            name='board_member',
            field=models.ForeignKey(null=True, blank=True, to='board.BoardMember'),
        ),
    ]
