# Generated by Django 4.0.4 on 2022-05-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0010_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.TextField(default='hi'),
        ),
    ]
