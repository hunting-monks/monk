# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20150923_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='photoUrl',
            new_name='photo',
        ),
    ]
