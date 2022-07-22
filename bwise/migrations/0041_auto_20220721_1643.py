# Generated by Django 3.0.8 on 2022-07-21 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0040_auto_20220721_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bwsmembership',
            name='Cellphone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='bwsmembership',
            name='Email',
            field=models.EmailField(error_messages={'unique': 'Another fellow has this email'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='last_used',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 14, 43, 49, 720489, tzinfo=utc), editable=False),
        ),
    ]
