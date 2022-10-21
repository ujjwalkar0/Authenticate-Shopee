# Generated by Django 4.1.1 on 2022-09-22 07:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_alter_orders_pin_no'),
        ('users', '0002_alter_users_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.deliveryagent')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
            ],
        ),
    ]