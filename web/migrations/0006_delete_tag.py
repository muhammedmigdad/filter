# Generated by Django 5.1.1 on 2024-09-12 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_size_product_sizs_alter_size_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
