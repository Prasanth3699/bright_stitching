# Generated by Django 4.1 on 2022-09-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_caps_image_alter_safetywears_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
