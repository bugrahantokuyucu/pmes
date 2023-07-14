# Generated by Django 4.2.2 on 2023-07-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0004_rename_number_of_remained_amount_workorder_remained_amount'),
        ('processes', '0003_remove_processlog_number_of_copy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processlog',
            name='work_order',
        ),
        migrations.AddField(
            model_name='processlog',
            name='work_order',
            field=models.ManyToManyField(related_name='work_order', to='work_orders.workorder'),
        ),
    ]