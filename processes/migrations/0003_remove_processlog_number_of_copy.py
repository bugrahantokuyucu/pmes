# Generated by Django 4.2.2 on 2023-07-14 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0002_rename_processlogs_processlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processlog',
            name='number_of_copy',
        ),
    ]
