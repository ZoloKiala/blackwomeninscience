# Generated by Django 3.0.8 on 2020-12-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0013_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BWSmentorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
                ('Cellphone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Age', models.CharField(choices=[('18-24', '18-24'), ('25-29', '25-29'), ('30-34', '30-34'), ('35-39', '35-39'), ('40-49', '40-49'), ('49 and older', '49 and older')], max_length=200)),
                ('Province', models.CharField(choices=[('Eastern Cape', 'Eastern Cape'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng'), ('KwaZulu-Natal', 'KwaZulu-Natal'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ('Northern Cape', 'Northern Cape'), ('Western Cape', 'Western Cape')], max_length=200)),
                ('Country', models.CharField(max_length=200)),
                ('Scientific_discipline', models.CharField(max_length=200)),
                ('Last_academic_qualification', models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma')], max_length=200)),
                ('Share_experience', models.CharField(max_length=400)),
                ('Description_idea', models.CharField(max_length=400)),
                ('Time_to_mentorship', models.CharField(choices=[('2 -5 hours', '2 -5 hours'), ('5-10 hours', '5-10 hours'), ('10-15 hours', '10-15 hours'), ('more than 15 hours', 'more than 15 hours')], max_length=200)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
