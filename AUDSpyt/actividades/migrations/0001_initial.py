# Generated by Django 2.1.2 on 2019-04-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcionCorta', models.CharField(max_length=250)),
                ('descripcionLarga', models.CharField(max_length=250)),
                ('icono', models.ImageField(upload_to='IconoActividad/')),
                ('fechaFinal', models.DateTimeField()),
                ('publicarInstagram', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=250)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.Activity')),
                ('userInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInfo.UserInfo')),
            ],
        ),
    ]
