# Generated by Django 5.0.2 on 2024-04-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pass_gen', '0002_password_password_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='password',
        ),
        migrations.AlterField(
            model_name='password',
            name='password_length',
            field=models.PositiveIntegerField(default=8),
        ),
    ]
