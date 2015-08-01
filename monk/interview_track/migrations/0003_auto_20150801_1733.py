# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview_track', '0002_auto_20150726_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='businessDescription',
            field=models.CharField(max_length=20, verbose_name=b'Business Description', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(max_length=2, verbose_name=b'State', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=50, verbose_name=b'Address', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Company Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='province',
            field=models.CharField(max_length=20, verbose_name=b'Province'),
        ),
        migrations.AlterField(
            model_name='company',
            name='zipcode',
            field=models.CharField(max_length=10, verbose_name=b'Zip'),
        ),
    ]
