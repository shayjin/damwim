# Generated by Django 4.0.4 on 2022-06-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0032_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='picture_url',
            field=models.TextField(default='?', null=True),
        ),
    ]