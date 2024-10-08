# Generated by Django 5.1.1 on 2024-09-08 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='download',
            old_name='title',
            new_name='video_title',
        ),
        migrations.RemoveField(
            model_name='download',
            name='url',
        ),
        migrations.AddField(
            model_name='download',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
