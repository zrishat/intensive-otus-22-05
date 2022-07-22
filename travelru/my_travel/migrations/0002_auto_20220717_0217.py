# Generated by Django 3.2 on 2022-07-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('HOTEL', 'Hotel'), ('AVIA', 'Avia')], default='HOTEL', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='defaultname', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
