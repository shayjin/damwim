# Generated by Django 4.0.4 on 2022-06-17 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0030_video_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='audio_url',
            field=models.TextField(default='?', null=True),
        ),
    ]