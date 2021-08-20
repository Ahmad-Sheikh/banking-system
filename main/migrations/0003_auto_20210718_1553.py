# Generated by Django 2.2.7 on 2021-07-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210718_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_type',
            field=models.CharField(choices=[('Business', 'Business'), ('Current', 'Current'), ('Saving', 'Saving')], help_text='Account Type', max_length=40),
        ),
    ]