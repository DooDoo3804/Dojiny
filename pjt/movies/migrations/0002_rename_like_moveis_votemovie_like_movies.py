# Generated by Django 3.2.13 on 2022-11-17 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='votemovie',
            old_name='like_moveis',
            new_name='like_movies',
        ),
    ]
