# Generated by Django 3.1.3 on 2020-12-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
