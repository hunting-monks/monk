# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20150927_1808'),
        ('interview_track', '0006_auto_20151006_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewscore',
            name='scored_by',
            field=models.ForeignKey(default=1, to='company.Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scorecardtemplate',
            name='created_by',
            field=models.ForeignKey(default=1, to='company.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score10',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score2',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score3',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score4',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score5',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score6',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score7',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score8',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score9',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
    ]
