# Generated by Django 3.1.7 on 2021-02-26 17:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0002_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trello_app.tasklist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 17, 15, 3, 889752, tzinfo=utc)),
        ),
    ]