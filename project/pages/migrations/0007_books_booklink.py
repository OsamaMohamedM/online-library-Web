# Generated by Django 5.0.6 on 2024-05-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_books_year_alter_books_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='booklink',
            field=models.ImageField(default='', upload_to='books'),
            preserve_default=False,
        ),
    ]
