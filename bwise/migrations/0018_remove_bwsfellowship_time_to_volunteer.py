# Generated by Django 3.0.8 on 2020-12-10 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0017_auto_20201210_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bwsfellowship',
            name='Time_to_volunteer',
        ),
    ]
