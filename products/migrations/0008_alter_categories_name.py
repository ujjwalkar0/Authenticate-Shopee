# Generated by Django 4.1.1 on 2022-09-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_name_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
