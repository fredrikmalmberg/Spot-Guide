# Generated by Django 2.2 on 2019-05-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0006_auto_20190508_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='destination',
        ),
        migrations.AddField(
            model_name='persona',
            name='destination',
            field=models.ManyToManyField(help_text='Select destinations where this persona would be happy to go', to='wizard.Destination'),
        ),
    ]
