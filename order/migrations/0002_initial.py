# Generated by Django 5.1.2 on 2024-10-28 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_orders', to='store.product'),
        ),
        migrations.AlterUniqueTogether(
            name='productorder',
            unique_together={('order', 'product')},
        ),
    ]
