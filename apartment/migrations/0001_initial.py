# Generated by Django 2.2.24 on 2021-08-20 03:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=514)),
                ('region', models.CharField(max_length=514)),
                ('cost', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)], verbose_name='')),
                ('room', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('infomation', models.TextField()),
            ],
        ),
    ]