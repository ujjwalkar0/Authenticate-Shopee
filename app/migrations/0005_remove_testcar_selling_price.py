# Generated by Django 3.1.5 on 2021-01-30 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_testcar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcar',
            name='selling_price',
        ),
    ]
