# Generated by Django 3.1.7 on 2021-02-26 17:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 2, 26, 17, 5, 38, 662379, tzinfo=utc))),
            ],
        ),
    ]
