# Generated by Django 4.2.7 on 2024-02-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodePalaceUsers', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg ', upload_to='profile_pic'),
        ),
    ]