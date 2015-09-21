# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20150919_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='area',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'Unknown'), (1, b'Accounting'), (2, b'Computer Hardware'), (3, b'Computer Software'), (4, b'Internet')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='current_end_date',
            field=models.DateField(default=datetime.datetime(1, 1, 1, 0, 0), blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='current_salary',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='current_start_date',
            field=models.DateField(default=datetime.datetime(1, 1, 1, 0, 0), blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='degree',
            field=models.IntegerField(choices=[(0, b'Unknown'), (1, b'Below BS'), (2, b'BS'), (3, b'MS'), (4, b'PHD')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='degree2',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'Unknown'), (1, b'Below BS'), (2, b'BS'), (3, b'MS'), (4, b'PHD')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='degree3',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'Unknown'), (1, b'Below BS'), (2, b'BS'), (3, b'MS'), (4, b'PHD')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='expected_salary',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='graduate_date',
            field=models.DateField(default=datetime.datetime(1, 1, 1, 0, 0), blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='level',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'Unknown'), (1, b'Entry'), (2, b'Junior'), (3, b'Senior'), (4, b'Veteran'), (5, b'Principle'), (6, b'Distinguished')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'avartars/', blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(default=b'', upload_to=b'resumes/', blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='source',
            field=models.IntegerField(choices=[(0, b'Unknown'), (1, b'Internal referral'), (2, b'Self submitted'), (3, b'Linkedin')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='area',
            field=models.IntegerField(choices=[(0, b'Unknown'), (1, b'Accounting'), (2, b'Computer Hardware'), (3, b'Computer Software'), (4, b'Internet')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name=b'Marital Status', choices=[(b'U', b'Unknown'), (b'S', b'Single'), (b'M', b'Married')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(0, b'U'), (1, b'M'), (2, b'F')]),
        ),
        migrations.AlterField(
            model_name='role',
            name='mask',
            field=models.BigIntegerField(choices=[(0, b'Unknown'), (1, b'Admin'), (4, b'Interviewer'), (8, b'HR'), (16, b'Hiring Manager')]),
        ),
    ]
