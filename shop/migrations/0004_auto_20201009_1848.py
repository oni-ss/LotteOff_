# Generated by Django 3.1.1 on 2020-10-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='unavailable',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]