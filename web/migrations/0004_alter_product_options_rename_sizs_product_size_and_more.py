# Generated by Django 5.1.1 on 2024-09-12 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_siz_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sizs',
            new_name='size',
        ),
        migrations.AlterModelTable(
            name='product',
            table='web_product',
        ),
    ]
