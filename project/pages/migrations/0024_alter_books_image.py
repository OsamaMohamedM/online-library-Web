# Generated by Django 5.0.6 on 2024-05-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_delete_image_alter_books_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='media/photo/'),
        ),
    ]
