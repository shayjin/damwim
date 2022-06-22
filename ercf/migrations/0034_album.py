# Generated by Django 4.0.4 on 2022-06-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0033_artist_picture_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture', models.ImageField(upload_to='images/')),
                ('picture_url', models.TextField(default='?', null=True)),
                ('des', models.TextField()),
            ],
        ),
    ]