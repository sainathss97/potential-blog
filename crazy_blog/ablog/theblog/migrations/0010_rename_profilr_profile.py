# Generated by Django 3.2 on 2021-06-15 13:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0009_profilr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profilr',
            new_name='Profile',
        ),
    ]