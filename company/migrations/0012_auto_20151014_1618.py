# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_auto_20151013_0430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='user',
        ),
        migrations.AlterField(
            model_name='role',
            name='mask',
            field=models.BigIntegerField(choices=[(b'r', b'r'), (b'w', b'w')]),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission',
            field=models.CharField(max_length=10, choices=[(0, b'Unknown'), (1, b'Admin'), (4, b'Interviewer'), (8, b'Recruiter'), (16, b'Hiring Manager')]),
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]
