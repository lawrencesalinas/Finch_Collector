# Generated by Django 4.0.1 on 2022-01-06 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_car_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.owner'),
        ),
    ]
