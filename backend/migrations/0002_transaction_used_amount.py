# Generated by Django 4.0.5 on 2022-07-14 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='used_amount',
            field=models.FloatField(default=0),
        ),
    ]