# Generated by Django 3.2.19 on 2023-06-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0006_alter_join_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
