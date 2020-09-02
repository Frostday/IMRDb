# Generated by Django 3.1 on 2020-09-01 09:32

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('stars', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
    ]