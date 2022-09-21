# Generated by Django 4.1.1 on 2022-09-19 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fields', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author_desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='km_driven',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='released_year',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='transmission',
        ),
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
        migrations.DeleteModel(
            name='Catagories',
        ),
    ]