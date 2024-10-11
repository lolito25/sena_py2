# Generated by Django 5.1.2 on 2024-10-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('foto', models.ImageField(null=True, upload_to='fotos/', verbose_name='Foto')),
                ('clase', models.TextField(null=True, verbose_name='Clase')),
            ],
        ),
    ]
