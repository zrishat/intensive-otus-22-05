# Generated by Django 3.2 on 2022-07-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_travel', '0007_auto_20220721_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='avia',
            name='airline',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='avia',
            name='city_from',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='avia',
            name='city_to',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='avia',
            name='departure_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='avia',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='avia',
            name='return_at',
            field=models.DateTimeField(null=True),
        ),
    ]
