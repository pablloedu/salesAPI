# Generated by Django 4.0.6 on 2022-07-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='units',
            field=models.IntegerField(default=1, verbose_name='Unit(s)'),
        ),
    ]
