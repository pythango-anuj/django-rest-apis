# Generated by Django 3.0.3 on 2022-01-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]