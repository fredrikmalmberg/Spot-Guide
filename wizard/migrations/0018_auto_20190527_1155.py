# Generated by Django 2.2 on 2019-05-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0017_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(max_length=500),
        ),
    ]
