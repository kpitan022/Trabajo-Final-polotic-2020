# Generated by Django 3.1.2 on 2020-11-23 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0032_auto_20201123_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinicaApp.paciente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicaApp.producto'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicaApp.medico'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicaApp.paciente'),
        ),
    ]
