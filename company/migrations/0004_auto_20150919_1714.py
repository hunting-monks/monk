# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_applicant_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='applicant',
            name='photo',
            field=models.FileField(default=b'', max_length=25, upload_to=b'', blank=True),
        ),
    ]
