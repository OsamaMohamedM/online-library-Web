# Generated by Django 5.0.6 on 2024-05-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_alter_books_num_of_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='tittle',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
