# Generated by Django 3.1.7 on 2021-03-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customerprofile'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.AddField(
            model_name='orders',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customerprofile'),
        ),
    ]