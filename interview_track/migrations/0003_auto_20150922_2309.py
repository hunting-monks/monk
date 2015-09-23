# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20150922_2309'),
        ('interview_track', '0002_auto_20150922_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(choices=[(1, b'Not started'), (2, b'Phone screen scheduled'), (3, b'Phone screen finished'), (4, b'Onsite scheduled'), (5, b'Onsite finished'), (6, b'Offered'), (7, b'Rejected'), (8, b'On hold')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(to='company.Applicant')),
            ],
        ),
        migrations.RemoveField(
            model_name='applicatecase',
            name='applicant_id',
        ),
        migrations.RemoveField(
            model_name='applicatecase',
            name='job_id',
        ),
        migrations.RenameField(
            model_name='interviewscore',
            old_name='interview_id',
            new_name='interview',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='case_id',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='interviewer_id',
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(default=1, to='company.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interview',
            name='comment',
            field=models.CharField(default=b'', max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='comment',
            field=models.CharField(default=b'', max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='evaluated_field',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='interviewscore',
            name='score',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='creator',
            field=models.ForeignKey(related_name='creator', to='company.Employee'),
        ),
        migrations.AlterField(
            model_name='job',
            name='hiring_manager',
            field=models.ForeignKey(related_name='hm', to='company.Employee'),
        ),
        migrations.AlterField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(related_name='recruiter', to='company.Employee'),
        ),
        migrations.DeleteModel(
            name='ApplicateCase',
        ),
        migrations.AddField(
            model_name='applicationcase',
            name='job',
            field=models.ForeignKey(to='interview_track.Job'),
        ),
        migrations.AddField(
            model_name='interview',
            name='case',
            field=models.ForeignKey(default=1, to='interview_track.ApplicationCase'),
            preserve_default=False,
        ),
    ]
