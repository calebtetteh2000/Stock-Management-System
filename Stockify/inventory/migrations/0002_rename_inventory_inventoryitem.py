# Generated by Django 5.0.7 on 2024-07-22 22:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventory',
            new_name='InventoryItem',
        ),
    ]
