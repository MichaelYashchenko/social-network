# Generated by Django 3.2.6 on 2021-09-05 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='avatar1',
        ),
    ]
