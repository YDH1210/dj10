# Generated by Django 4.1.2 on 2022-11-02 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='Comment',
            new_name='comment',
        ),
    ]