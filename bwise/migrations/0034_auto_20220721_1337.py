# Generated by Django 3.0.8 on 2022-07-21 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bwise', '0033_auto_20220604_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='bwsfellowship',
            name='City_o',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bwsfellowship',
            name='Country_o',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bwsfellowship',
            name='Province',
            field=models.CharField(choices=[('Eastern Cape', 'Eastern Cape'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng'), ('KwaZulu-Natal', 'KwaZulu-Natal'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ('Northern Cape', 'Northern Cape'), ('Western Cape', 'Western Cape'), ('Outside South Africa', 'Outside South Africa')], max_length=200),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='last_used',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 11, 37, 7, 198944, tzinfo=utc), editable=False),
        ),
    ]