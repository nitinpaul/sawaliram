# Generated by Django 2.2.3 on 2020-04-23 19:14

import dashboard.mixins.draftables
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_auto_20200417_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover_image',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
