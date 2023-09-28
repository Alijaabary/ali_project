# Generated by Django 4.2.3 on 2023-07-27 11:15

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_1', models.CharField(blank=True, max_length=128)),
                ('adress_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('state', localflavor.us.models.USStateField(default='NY', max_length=2)),
                ('zipcde', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
            ],
        ),
    ]
