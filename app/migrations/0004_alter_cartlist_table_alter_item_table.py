# Generated by Django 4.1.3 on 2022-12-29 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cartlist_item'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cartlist',
            table='cartlist',
        ),
        migrations.AlterModelTable(
            name='item',
            table='item',
        ),
    ]