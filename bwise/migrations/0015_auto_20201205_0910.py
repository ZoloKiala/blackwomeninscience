# Generated by Django 3.0.8 on 2020-12-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0014_bwsmentorship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bwsmentorship',
            name='Time_to_mentorship',
            field=models.CharField(choices=[('2-5 hours', '2-5 hours'), ('5-10 hours', '5-10 hours'), ('10-15 hours', '10-15 hours'), ('more than 15 hours', 'more than 15 hours')], max_length=200),
        ),
    ]