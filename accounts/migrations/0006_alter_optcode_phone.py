# Generated by Django 5.0.3 on 2024-03-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optcode',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
