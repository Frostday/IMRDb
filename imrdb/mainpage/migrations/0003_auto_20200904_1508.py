# Generated by Django 3.1 on 2020-09-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
