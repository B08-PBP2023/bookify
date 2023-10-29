# Generated by Django 4.2.4 on 2023-10-28 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinjamBuku', '0002_auto_20231024_2352'),
        ('profilUser', '0003_rename_user_userprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinjamBuku.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]