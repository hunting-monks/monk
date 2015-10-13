# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20150927_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='size',
            field=models.IntegerField(default=1, verbose_name=b'Size'),
        ),
        migrations.AddField(
            model_name='employee',
            name='isRegistered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='area',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'Unknown'), (1, b'Accounting'), (2, b'Computer Hardware'), (3, b'Computer Software'), (4, b'Internet')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'City', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='province',
            field=models.CharField(max_length=20, verbose_name=b'Province', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(related_name='employee', to='company.Role', null=True),
        ),
    ]
