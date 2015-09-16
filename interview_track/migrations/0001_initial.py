# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicateCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(choices=[(1, b'Not started'), (2, b'Phone screen scheduled'), (3, b'Phone screen finished'), (4, b'Onsite scheduled'), (5, b'Onsite finished'), (6, b'Offered'), (7, b'Rejected'), (8, b'On hold')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('applicant_id', models.ForeignKey(to='company.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(choices=[(1, b'Phone screen'), (2, b'Onsite coding'), (3, b'Onsite HR'), (4, b'Onsite HM')])),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, b'Scheduled'), (2, b'Candidate Confirmed'), (3, b'Interviewer Confirmed'), (4, b'Passed'), (5, b'Rejected')])),
                ('comment', models.CharField(max_length=2000)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('case_id', models.ForeignKey(to='interview_track.ApplicateCase')),
                ('interviewer_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluated_field', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('comment', models.CharField(max_length=2000)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('interview_id', models.ForeignKey(to='interview_track.Interview')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('area', models.IntegerField(choices=[(1, b'Accounting'), (2, b'Computer Hardware'), (3, b'Computer Software'), (4, b'Internet')])),
                ('level', models.IntegerField(choices=[(1, b'Entry'), (2, b'Junior'), (3, b'Senior'), (4, b'Veteran'), (5, b'Principle'), (6, b'Distinguished')])),
                ('description', models.CharField(max_length=5000)),
                ('salary_high', models.IntegerField()),
                ('salary_low', models.IntegerField()),
                ('expire_date', models.DateField()),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_id', models.ForeignKey(to='company.Company')),
                ('creator_id', models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('hiring_manager_id', models.ForeignKey(related_name='hm', to=settings.AUTH_USER_MODEL)),
                ('recruiter_id', models.ForeignKey(related_name='recruiter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='applicatecase',
            name='job_id',
            field=models.ForeignKey(to='interview_track.Job'),
        ),
    ]
