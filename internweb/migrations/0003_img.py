# Generated by Django 5.0.6 on 2024-05-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internweb', '0002_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
