# Generated by Django 3.2.7 on 2021-11-08 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_auto_20211108_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_outlet.author'),
        ),
    ]
