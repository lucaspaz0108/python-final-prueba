# Generated by Django 4.1.2 on 2022-12-09 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_marca_alter_deporte_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.marca'),
        ),
    ]