# Generated by Django 4.2.1 on 2023-05-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findCar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zip',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]