# Generated by Django 3.1.2 on 2020-11-18 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0012_pedido_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'pedido', 'verbose_name_plural': 'pedidos'},
        ),
    ]