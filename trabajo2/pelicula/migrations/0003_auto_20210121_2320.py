# Generated by Django 3.1.2 on 2021-01-22 02:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0002_pelicula_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
