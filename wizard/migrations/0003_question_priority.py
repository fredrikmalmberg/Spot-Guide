# Generated by Django 2.2 on 2019-05-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0002_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='priority',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
    ]
