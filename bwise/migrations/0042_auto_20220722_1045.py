# Generated by Django 3.0.8 on 2022-07-22 08:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0041_auto_20220721_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bwsmembership',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='last_used',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 8, 45, 47, 740767, tzinfo=utc), editable=False),
        ),
    ]
