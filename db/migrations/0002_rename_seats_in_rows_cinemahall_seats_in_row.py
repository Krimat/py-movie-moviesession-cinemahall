# Generated by Django 4.0.2 on 2022-03-15 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='seats_in_rows',
            new_name='seats_in_row',
        ),
    ]