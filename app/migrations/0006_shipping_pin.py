# Generated by Django 4.1.3 on 2023-01-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='pin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
