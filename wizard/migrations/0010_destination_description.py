# Generated by Django 2.2 on 2019-05-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0009_auto_20190508_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.CharField(default='No description has yet been written for this destination', help_text='Enter a description for this destination', max_length=200),
        ),
    ]
