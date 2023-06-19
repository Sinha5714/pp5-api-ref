# Generated by Django 3.2.19 on 2023-06-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0007_join_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]