# Generated by Django 4.0.4 on 2022-06-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0034_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.TextField(default='?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.TextField(default='?'),
            preserve_default=False,
        ),
    ]
