# Generated by Django 4.1.1 on 2022-09-14 15:49

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='items')),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('desc', ckeditor.fields.RichTextField()),
                ('post_date', models.DateField(auto_now_add=True)),
                ('Pin_No', models.IntegerField()),
                ('released_year', models.IntegerField(null=True)),
                ('km_driven', models.IntegerField(null=True)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Electric', 'Electric'), ('LPG', 'LPG')], max_length=255, null=True)),
                ('seller_type', models.CharField(max_length=255, null=True)),
                ('transmission', models.CharField(max_length=255, null=True)),
                ('owner', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(null=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.catagories')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
