# Generated by Django 3.2.19 on 2023-06-14 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('join', '0003_auto_20230612_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join', to='events.event'),
        ),
        migrations.AlterUniqueTogether(
            name='join',
            unique_together={('user', 'event')},
        ),
        migrations.RemoveField(
            model_name='join',
            name='email',
        ),
        migrations.RemoveField(
            model_name='join',
            name='name',
        ),
        migrations.RemoveField(
            model_name='join',
            name='reason',
        ),
    ]