# Generated by Django 4.2.6 on 2023-10-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0002_questionanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='judul_buku',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='judul_buku',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
