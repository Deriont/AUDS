# Generated by Django 2.1.2 on 2019-03-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosasSeguridad', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido1', models.CharField(max_length=250)),
                ('apellido2', models.CharField(max_length=250)),
                ('DNI', models.CharField(max_length=250)),
                ('fecha_nacimiento', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('modalidad', models.CharField(max_length=250)),
                ('estilo', models.CharField(max_length=250)),
                ('skatepark', models.CharField(max_length=250)),
                ('fecha', models.CharField(max_length=250)),
                ('residencia', models.CharField(max_length=250)),
            ],
        ),
    ]