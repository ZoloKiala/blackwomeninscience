# Generated by Django 3.0.8 on 2022-06-01 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0029_auto_20211002_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='last_used',
            field=models.DateTimeField(default=datetime.date(2022, 6, 1), editable=False),
        ),
    ]
