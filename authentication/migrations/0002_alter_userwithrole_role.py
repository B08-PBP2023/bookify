from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithrole',
            name='role',
            field=models.CharField(choices=[('Reguler', 'Reguler'), ('Special', 'Special')], max_length=10),
        ),
    ]