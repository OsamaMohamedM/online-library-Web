# Generated by Django 5.0.6 on 2024-05-16 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_image_alter_books_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'books'},
        ),
    ]
