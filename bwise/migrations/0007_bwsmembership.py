# Generated by Django 3.0.8 on 2020-11-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0006_auto_20201114_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='BWSmembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
                ('Gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=200)),
                ('Cellphone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Age', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=200)),
                ('Province', models.CharField(choices=[('Eastern Cape', 'Eastern Cape'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng'), ('KwaZulu-Natal', 'KwaZulu-Natal'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ('Northern Cape', 'Northern Cape'), ('Western Cape', 'Western Cape')], max_length=200)),
                ('University', models.CharField(max_length=200)),
                ('Race', models.CharField(choices=[('african', 'african'), ('white', 'white'), ('indian', 'indian'), ('color', 'color')], max_length=200)),
                ('Country', models.CharField(max_length=200)),
                ('Town_attend_workshops', models.CharField(choices=[('Johannesburg', 'Johannesburg'), ('Durban', 'Durban'), ('indian', 'indian'), ('Webinar', 'Webinar')], max_length=200)),
                ('Last_academic_qualification', models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma')], max_length=200)),
                ('Current_academic_qualification', models.CharField(choices=[('Post PhD', 'Post PhD'), ('PhD', 'PhD'), ('Masters', 'Masters'), ('Honours', 'Honours'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma')], max_length=200)),
                ('Scientific_discipline', models.CharField(max_length=200)),
                ('Subject_major', models.CharField(max_length=200)),
                ('Occupation', models.CharField(max_length=200)),
                ('Where_hear_organisation', models.CharField(max_length=200)),
                ('Interested_mentorship_programs', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=200)),
                ('Time_to_volunteer', models.CharField(choices=[('up to 2 hrs', 'up to 2 hrs'), ('up to 4 hrs', 'up to 4 hrs'), ('up to 6 hrs', 'up to 6 hrs'), ('1 full day', '1 full day')], max_length=200)),
                ('Conducted_TV_interview', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
