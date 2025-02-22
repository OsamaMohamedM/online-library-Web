# Generated by Django 5.0.6 on 2024-05-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('tittle', models.CharField(max_length=30)),
                ('des', models.TextField()),
                ('numofpage', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('image', models.ImageField(upload_to='photo')),
                ('active', models.BooleanField(default=True)),
                ('category', models.CharField(blank=True, choices=[('function', 'function')], max_length=30, null=True)),
                ('author', models.CharField(max_length=50)),
                ('lan', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'books',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=18)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=5)),
                ('borrowedBooks', models.ManyToManyField(null=True, to='pages.books')),
            ],
            options={
                'verbose_name': 'users',
            },
        ),
    ]
