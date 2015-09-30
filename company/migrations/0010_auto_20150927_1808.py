# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20150923_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(unique=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(unique=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='mask',
            field=models.BigIntegerField(choices=[(0, b'Unknown'), (1, b'Admin'), (4, b'Interviewer'), (8, b'Recruiter'), (16, b'Hiring Manager')]),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
