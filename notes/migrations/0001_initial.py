# Generated by Django 4.2.2 on 2023-07-01 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_orders.workorder')),
            ],
            options={
                'verbose_name_plural': 'Notlar',
            },
        ),
    ]
