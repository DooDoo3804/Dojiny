# Generated by Django 3.2.13 on 2022-11-16 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=200)),
                ('movie_id', models.IntegerField()),
                ('original_title', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('overview', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=50)),
                ('vote_average', models.IntegerField()),
                ('director', models.CharField(max_length=50)),
                ('poster_path', models.CharField(max_length=50)),
                ('backdrop_path', models.CharField(max_length=50)),
                ('runtime', models.IntegerField()),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
