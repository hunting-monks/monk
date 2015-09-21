# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20150919_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='resume_path',
        ),
        migrations.AddField(
            model_name='applicant',
            name='resume',
            field=models.FileField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.ImageField(default=b'', max_length=25, upload_to=b'', blank=True),
        ),
    ]
