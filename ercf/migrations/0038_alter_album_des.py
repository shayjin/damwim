# Generated by Django 4.0.4 on 2022-06-22 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0037_alter_album_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='des',
            field=models.CharField(max_length=1024),
        ),
    ]