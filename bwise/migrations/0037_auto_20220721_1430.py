# Generated by Django 3.0.8 on 2022-07-21 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0036_auto_20220721_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='last_used',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 12, 30, 32, 482325, tzinfo=utc), editable=False),
        ),
    ]
