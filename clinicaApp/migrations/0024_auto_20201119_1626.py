# Generated by Django 3.1.2 on 2020-11-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0023_auto_20201119_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial_medico',
            old_name='historial_medico',
            new_name='historial_id',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='historial_medico',
        ),
        migrations.AddField(
            model_name='turno',
            name='concurrio',
            field=models.BooleanField(null=True),
        ),
    ]
