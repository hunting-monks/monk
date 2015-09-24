# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20150922_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default='2015-09-23', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(default=1, to='company.Role'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(default='2015-09-23', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='level',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'Unknown'), (1, b'Entry'), (2, b'Junior'), (3, b'Senior'), (4, b'Principle'), (5, b'Distinguished')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Company Name', db_index=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address2',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(default=b'', max_length=35, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(default=b'U', choices=[(b'U', b'Unknown'), (b'S', b'Single'), (b'M', b'Married')], max_length=2, blank=True, null=True, verbose_name=b'Marital Status'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middleInitial',
            field=models.CharField(default=b'', max_length=1, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=b'', max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'U'), (1, b'M'), (2, b'F')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(default=b'Act', max_length=3, choices=[(b'Ped', b'Pending'), (b'Act', b'Active'), (b'Del', b'Deleted')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zip',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
    ]
