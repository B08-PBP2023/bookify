# Generated by Django 4.2.6 on 2023-10-29 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestBuku', '0002_buku_remove_bookrequest_book_remove_bookrequest_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buku',
            new_name='BukuReq',
        ),
    ]
