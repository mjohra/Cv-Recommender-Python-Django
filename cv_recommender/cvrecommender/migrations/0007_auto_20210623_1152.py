# Generated by Django 3.1.7 on 2021-06-23 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvrecommender', '0006_auto_20210619_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='total_experience_application',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
    ]
