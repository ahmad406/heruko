# Generated by Django 3.1.3 on 2020-12-08 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tec', '0003_auto_20201207_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='mail',
        ),
    ]
