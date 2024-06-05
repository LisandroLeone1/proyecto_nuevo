# Generated by Django 5.0.4 on 2024-06-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_alter_servicios_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='servicios',
            name='contenido',
        ),
        migrations.AddField(
            model_name='servicios',
            name='contenido',
            field=models.ManyToManyField(to='servicios.funciones'),
        ),
    ]
