# Generated by Django 4.2.1 on 2023-05-30 08:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.CharField(max_length=2)),
                ('state_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('zip', models.IntegerField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findCar.state')),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county_fips', models.CharField(max_length=5)),
                ('county_name', models.CharField(max_length=100)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='findCar.location')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_lat', models.FloatField()),
                ('pickup_lng', models.FloatField()),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('description', models.TextField()),
                ('zipCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findCar.location')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, unique=True)),
                ('carrying_capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findCar.location')),
            ],
        ),
    ]