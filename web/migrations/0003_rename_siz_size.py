# Generated by Django 5.1.1 on 2024-09-11 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_tag_remove_product_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='siz',
            new_name='Size',
        ),
    ]
