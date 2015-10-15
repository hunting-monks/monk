# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20151014_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(related_name='employees', to='company.Role', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('name', 'permission', 'mask')]),
        ),
    ]
