# Generated by Django 5.0.6 on 2024-05-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_books_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
