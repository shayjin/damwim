# Generated by Django 4.0.4 on 2022-05-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0016_review_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='post_title',
        ),
        migrations.AlterField(
            model_name='review',
            name='post_id',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]