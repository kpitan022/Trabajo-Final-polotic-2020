# Generated by Django 3.1.2 on 2020-11-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0042_auto_20201127_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_gerencia', 'Puede ver el gerencia'),),
            },
        ),
    ]
