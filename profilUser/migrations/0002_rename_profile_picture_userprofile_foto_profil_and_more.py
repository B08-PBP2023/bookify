# Generated by Django 4.2.4 on 2023-10-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_picture',
            new_name='foto_profil',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tanggal_lahir',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
