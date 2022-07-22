# Generated by Django 3.2 on 2022-07-16 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=40)),
                ('city_to', models.CharField(max_length=40)),
                ('date_beg', models.DateField()),
                ('time_beg', models.TimeField()),
                ('date_end', models.DateField()),
                ('time_end', models.TimeField()),
                ('price', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='my_travel.item')),
            ],
        ),
        migrations.CreateModel(
            name='Avia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='my_travel.item')),
            ],
        ),
    ]
