# Generated by Django 3.2.7 on 2021-10-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('number_of_seats', models.IntegerField(verbose_name='number of seats')),
                ('trip_date', models.DateTimeField(verbose_name='trip date')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': 'carTrip',
                'verbose_name_plural': 'cartrips',
            },
        ),
    ]
