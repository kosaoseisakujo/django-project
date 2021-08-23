# Generated by Django 2.2.24 on 2021-08-20 07:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_apartment_features_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='main_flag',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name=''),
        ),
    ]
