# Generated by Django 3.2.19 on 2023-06-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Discrimination', 'Descrimination'), ('LQBTQ', 'LGBTQ'), ('Equal-Rights', 'Equal Rights'), ('Marraige-Rights', 'Marraige Rights'), ('Work-Rights', 'Work Rights'), ('Education-Rights', 'Education Rights')], default='Equal-Rights', max_length=50),
        ),
    ]
