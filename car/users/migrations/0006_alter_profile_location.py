# Generated by Django 4.2.3 on 2023-07-28 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]
