# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='created_by_company',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='created_by_user',
        ),
        migrations.AddField(
            model_name='applicant',
            name='created_by',
            field=models.ForeignKey(related_name='author', default=1, to='company.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address2',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='zipcode',
            field=models.CharField(max_length=10, verbose_name=b'Zip', blank=True),
        ),
    ]
