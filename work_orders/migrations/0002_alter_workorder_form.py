# Generated by Django 4.2.2 on 2023-07-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='form',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
