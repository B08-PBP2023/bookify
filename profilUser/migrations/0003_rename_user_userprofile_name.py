# Generated by Django 4.2.4 on 2023-10-27 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilUser', '0002_rename_profile_picture_userprofile_foto_profil_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='name',
        ),
    ]
