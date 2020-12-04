# Generated by Django 3.0.8 on 2020-11-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0004_otherpicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('province', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
            ],
        ),
    ]