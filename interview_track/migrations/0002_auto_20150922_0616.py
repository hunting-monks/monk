# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interview_track', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='hiring_manager_id',
            new_name='hiring_manager',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='recruiter_id',
            new_name='recruiter',
        ),
        migrations.AddField(
            model_name='applicatecase',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(1, 1, 1, 0, 0), blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_high',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_low',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
