# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview_track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('area', models.IntegerField(choices=[(1, b'Accounting'), (2, b'Computer Hardware'), (3, b'Computer Software'), (4, b'Internet')])),
                ('level', models.IntegerField(choices=[(1, b'Entry'), (2, b'Junior'), (3, b'Senior'), (4, b'Veteran'), (5, b'Principle'), (6, b'Distinguished')])),
                ('expected_salary', models.IntegerField()),
                ('current_salary', models.IntegerField()),
                ('resume_path', models.CharField(max_length=100)),
                ('current_company', models.CharField(max_length=200)),
                ('current_title', models.CharField(max_length=50)),
                ('current_start_date', models.DateField()),
                ('current_end_date', models.DateField()),
                ('prev_company1', models.CharField(max_length=200)),
                ('prev_title1', models.CharField(max_length=50)),
                ('prev_start_date1', models.DateField()),
                ('prev_end_date1', models.DateField()),
                ('prev_company2', models.CharField(max_length=200)),
                ('prev_title2', models.CharField(max_length=50)),
                ('prev_start_date2', models.DateField()),
                ('prev_end_date2', models.DateField()),
                ('prev_company3', models.CharField(max_length=200)),
                ('prev_title3', models.CharField(max_length=50)),
                ('prev_start_date3', models.DateField()),
                ('prev_end_date3', models.DateField()),
                ('graduate_school', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=10)),
                ('graduate_date', models.DateField()),
                ('graduate_school2', models.CharField(max_length=50)),
                ('degree2', models.CharField(max_length=10)),
                ('graduate_date2', models.DateField()),
                ('graduate_school3', models.CharField(max_length=50)),
                ('degree3', models.CharField(max_length=10)),
                ('graduate_date3', models.DateField()),
                ('source', models.IntegerField(choices=[(1, b'Internal referral'), (2, b'Self submitted'), (3, b'Linkedin')])),
                ('source_id', models.BigIntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicateCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(choices=[(1, b'Not started'), (2, b'Phone screen scheduled'), (3, b'Phone screen finished'), (4, b'Onsite scheduled'), (5, b'Onsite finished'), (6, b'Offered'), (7, b'Rejected'), (8, b'On hold')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('applicant_id', models.ForeignKey(to='interview_track.Applicant')),
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
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='mask',
            field=models.BigIntegerField(choices=[(1, b'Admin'), (4, b'Interviewer'), (8, b'HR'), (16, b'Hiring Manager')]),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='company_id',
            field=models.ForeignKey(to='interview_track.Company'),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='role_id',
            field=models.ForeignKey(to='interview_track.Role'),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='company_id',
            field=models.ForeignKey(to='interview_track.Company'),
        ),
        migrations.AddField(
            model_name='job',
            name='creator_id',
            field=models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='hiring_manager_id',
            field=models.ForeignKey(related_name='hm', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='recruiter_id',
            field=models.ForeignKey(related_name='recruiter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicatecase',
            name='job_id',
            field=models.ForeignKey(to='interview_track.Job'),
        ),
    ]
