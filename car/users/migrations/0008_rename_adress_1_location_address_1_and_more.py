# Generated by Django 4.2.3 on 2023-08-10 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='adress_1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='adress_2',
            new_name='address_2',
        ),
    ]