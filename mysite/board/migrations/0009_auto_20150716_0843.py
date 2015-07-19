# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_cadastre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardmember',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='cadastre',
            options={'ordering': ['cadastre_name']},
        ),
        migrations.RenameField(
            model_name='cadastre',
            old_name='cadsatre_name',
            new_name='cadastre_name',
        ),
    ]
