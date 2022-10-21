# Generated by Django 4.1.1 on 2022-09-21 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0008_alter_categories_name'),
        ('business', '0002_alter_shop_email_id_alter_shop_phone_no'),
        ('customer', '0002_customer_address_customer_district_customer_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_no', models.IntegerField(default=None)),
                ('is_accepted', models.BooleanField(default=None, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.shop')),
            ],
        ),
    ]