# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('idNoti', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('textoNoti', models.TextField(max_length=500)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(upload_to='/tmp')),
            ],
        ),
    ]
