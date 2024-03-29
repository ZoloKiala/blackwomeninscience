# Generated by Django 3.0.8 on 2020-12-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0018_remove_bwsfellowship_time_to_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bwsfellowship',
            name='Current_academic_qualification',
            field=models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('None', 'None')], max_length=200),
        ),
        migrations.AlterField(
            model_name='bwsfellowship',
            name='Last_academic_qualification',
            field=models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('None', 'None')], max_length=200),
        ),
        migrations.AlterField(
            model_name='bwsmembership',
            name='Current_academic_qualification',
            field=models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('None', 'None')], max_length=200),
        ),
        migrations.AlterField(
            model_name='bwsmembership',
            name='Last_academic_qualification',
            field=models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('None', 'None')], max_length=200),
        ),
    ]
