# Generated by Django 3.0.8 on 2020-11-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0011_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='bwsmembership',
            name='media_handle',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bwsmembership',
            name='Where_hear_organisation',
            field=models.CharField(choices=[('social media', 'Social media'), ('radio', 'Radio'), ('friend', 'Friend'), ('colleague', 'Colleague'), ('university', 'University')], max_length=200),
        ),
    ]
