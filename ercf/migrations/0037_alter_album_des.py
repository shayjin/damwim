# Generated by Django 4.0.4 on 2022-06-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0036_alter_album_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='des',
            field=models.TextField(),
        ),
    ]
