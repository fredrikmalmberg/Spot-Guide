# Generated by Django 2.2 on 2019-06-10 09:33

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0022_auto_20190607_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbbackup',
            name='dbbackup',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/does/not/matter/', location='/Users/user/django_apps/db_back'), upload_to='all_db_backups'),
        ),
    ]
