# Generated by Django 5.0.6 on 2024-05-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_books_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='booklink',
            field=models.ImageField(default=' ', upload_to='books'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='des',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='books',
            name='lan',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='books',
            name='numofpage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='books',
            name='tittle',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.CharField(max_length=5),
        ),
    ]
