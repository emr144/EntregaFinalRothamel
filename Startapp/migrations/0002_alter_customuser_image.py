# Generated by Django 5.0.6 on 2024-06-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
