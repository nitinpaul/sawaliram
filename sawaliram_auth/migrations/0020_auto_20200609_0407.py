# Generated by Django 2.2.3 on 2020-06-08 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sawaliram_auth', '0019_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='question',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='dashboard.Question'),
        ),
    ]
