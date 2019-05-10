# Generated by Django 2.1.2 on 2019-04-25 15:23

from django.db import migrations, models
import django.db.models.deletion


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
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('modalidad', models.CharField(choices=[('Skate', 'Skateboarding'), ('BMX', 'BMX'), ('Roller', 'Rollerbladin')], max_length=250)),
                ('estilo', models.CharField(choices=[('Rampa', 'Rampa'), ('Calle', 'Calle'), ('Ambas', 'Ambas')], max_length=250)),
                ('skatepark', models.CharField(max_length=250)),
                ('residencia', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('contacto', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='userInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInfo.UserInfo'),
        ),
    ]
