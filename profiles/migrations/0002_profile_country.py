# Generated by Django 3.2.19 on 2023-06-07 09:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
