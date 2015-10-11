# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview_track', '0007_auto_20151006_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewscore',
            name='template',
        ),
        migrations.AddField(
            model_name='interview',
            name='template',
            field=models.ForeignKey(default=1, to='interview_track.ScoreCardTemplate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='interview',
            field=models.OneToOneField(to='interview_track.Interview'),
        ),
        migrations.AlterField(
            model_name='scorecardtemplate',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=100),
        ),
    ]
