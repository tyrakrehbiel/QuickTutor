# Generated by Django 3.0.2 on 2020-04-15 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200414_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='rating_score',
            new_name='avg_rating',
        ),
    ]