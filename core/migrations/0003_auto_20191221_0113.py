# Generated by Django 3.0.1 on 2019-12-21 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='nome',
            new_name='nomemarca',
        ),
    ]
