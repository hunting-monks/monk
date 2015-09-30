# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20150927_1808'),
        ('interview_track', '0003_auto_20150922_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcase',
            name='creator',
            field=models.ForeignKey(default=1, to='company.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='area',
            field=models.IntegerField(choices=[(0, b'Unknown'), (1, b'Accounting'), (2, b'Computer Hardware'), (3, b'Computer Software'), (4, b'Internet')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='level',
            field=models.IntegerField(choices=[(0, b'Unknown'), (1, b'Entry'), (2, b'Junior'), (3, b'Senior'), (4, b'Principle'), (5, b'Distinguished')]),
        ),
    ]
