# Generated by Django 5.0 on 2024-10-08 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0033_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftDrink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='softdrinks/')),
                ('size', models.CharField(max_length=50)),
                ('availability', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryid', to='myadmin.product_category')),
            ],
            options={
                'db_table': 'softdrink',
            },
        ),
    ]