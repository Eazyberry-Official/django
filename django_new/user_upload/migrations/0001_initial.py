# Generated by Django 3.1.3 on 2020-12-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_uploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default='')),
                ('price', models.TextField(default='')),
                ('image', models.ImageField(default='', upload_to='products/')),
            ],
        ),
    ]