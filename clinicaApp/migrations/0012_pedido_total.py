# Generated by Django 3.1.2 on 2020-11-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0011_pedido_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
