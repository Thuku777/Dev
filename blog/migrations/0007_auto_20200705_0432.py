# Generated by Django 3.0.8 on 2020-07-05 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_repy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='repy',
            new_name='reply',
        ),
    ]
