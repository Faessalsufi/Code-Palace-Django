# Generated by Django 4.2.7 on 2024-02-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodePalaceUsers', '0003_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='check.png', upload_to='profile_pic'),
        ),
    ]