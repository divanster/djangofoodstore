# Generated by Django 4.2 on 2024-05-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_views_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_price',
        ),
    ]