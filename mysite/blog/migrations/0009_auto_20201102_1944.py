# Generated by Django 3.1 on 2020-11-02 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201102_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 2, 19, 44, 10, 421692, tzinfo=utc)),
        ),
    ]
