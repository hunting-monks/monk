# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interview_track', '0004_auto_20150927_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='interview_date',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='interview',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='interview',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
