# Generated by Django 2.2.3 on 2019-09-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sawaliram_auth', '0010_auto_20190909_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intro_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organisation_role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='ProfileSettings',
        ),
    ]
