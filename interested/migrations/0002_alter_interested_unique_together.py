# Generated by Django 3.2.19 on 2023-06-10 10:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_sub_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interested', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='interested',
            unique_together={('user', 'event')},
        ),
    ]
