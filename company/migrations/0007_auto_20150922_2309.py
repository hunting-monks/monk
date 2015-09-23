# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20150920_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='userdetail',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='userdetail',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='degree2',
            field=models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Below BS'), (2, b'BS'), (3, b'MS'), (4, b'PHD')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='degree3',
            field=models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Below BS'), (2, b'BS'), (3, b'MS'), (4, b'PHD')]),
        ),
    ]
