# Generated by Django 3.2 on 2022-06-21 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('db_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name_rus', models.CharField(max_length=100, unique=True)),
                ('name_eng', models.CharField(max_length=100, null=True, unique=True)),
                ('code_eng', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_aviasales', models.PositiveIntegerField(default=0, null=True)),
                ('name_rus', models.CharField(max_length=70, primary_key=True, serialize=False, unique=True)),
                ('name_eng', models.CharField(max_length=70, null=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='waysearch.country')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rus', models.CharField(max_length=70, unique=True)),
                ('name_eng', models.CharField(max_length=70, null=True, unique=True)),
                ('code_IATA', models.CharField(max_length=3, null=True, unique=True)),
                ('code_ICAO', models.CharField(max_length=4, null=True, unique=True)),
                ('code_rus', models.CharField(max_length=3, null=True, unique=True)),
                ('city', models.ForeignKey(default='Москва', on_delete=django.db.models.deletion.CASCADE, to='waysearch.city')),
            ],
        ),
    ]