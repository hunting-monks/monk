# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interview_track', '0005_auto_20150927_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCardTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('field1', models.CharField(default=b'', max_length=500)),
                ('field2', models.CharField(default=b'', max_length=500, blank=True)),
                ('field3', models.CharField(default=b'', max_length=500, blank=True)),
                ('field4', models.CharField(default=b'', max_length=500, blank=True)),
                ('field5', models.CharField(default=b'', max_length=500, blank=True)),
                ('field6', models.CharField(default=b'', max_length=500, blank=True)),
                ('field7', models.CharField(default=b'', max_length=500, blank=True)),
                ('field8', models.CharField(default=b'', max_length=500, blank=True)),
                ('field9', models.CharField(default=b'', max_length=500, blank=True)),
                ('field10', models.CharField(default=b'', max_length=500, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='interviewscore',
            old_name='score',
            new_name='score10',
        ),
        migrations.RemoveField(
            model_name='interviewscore',
            name='evaluated_field',
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score1',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score2',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score3',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score4',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score5',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score6',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score7',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score8',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='score9',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationcase',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Not started'), (2, b'Phone screen scheduled'), (3, b'Phone screen finished'), (4, b'Onsite scheduled'), (5, b'Onsite finished'), (6, b'Offered'), (7, b'Rejected'), (8, b'On hold')]),
        ),
        migrations.AlterField(
            model_name='interview',
            name='category',
            field=models.IntegerField(choices=[(b'', b'Interview type'), (1, b'Phone screen'), (2, b'Onsite'), (3, b'Onsite with HR'), (4, b'Onsite with HM')]),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Scheduled'), (2, b'Candidate Confirmed'), (3, b'Interviewer Confirmed'), (4, b'Passed'), (5, b'Rejected')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='expire_date',
            field=models.DateField(default=datetime.date(1, 1, 1), blank=True),
        ),
        migrations.AddField(
            model_name='interviewscore',
            name='template',
            field=models.ForeignKey(default=1, to='interview_track.ScoreCardTemplate'),
            preserve_default=False,
        ),
    ]
