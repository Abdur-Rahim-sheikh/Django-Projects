# Generated by Django 3.2.7 on 2021-11-17 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211110_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]