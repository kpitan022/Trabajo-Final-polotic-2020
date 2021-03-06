# Generated by Django 3.1.2 on 2020-11-19 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0022_auto_20201119_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_medico',
            name='historial_medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='clinicaApp.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='historial_medico',
            field=models.TextField(blank=True, null=True),
        ),
    ]
