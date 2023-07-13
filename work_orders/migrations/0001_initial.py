# Generated by Django 4.2.2 on 2023-07-01 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machines', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('form', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('number_of_blocks', models.IntegerField()),
                ('number_of_copy', models.DecimalField(decimal_places=1, max_digits=5)),
                ('number_of_remained_copy', models.DecimalField(decimal_places=1, max_digits=5)),
                ('priority', models.CharField(default='low', max_length=20)),
                ('status', models.CharField(default='waiting', max_length=20)),
                ('planned_start_date', models.DateField()),
                ('planned_end_date', models.DateField()),
                ('actual_start_date', models.DateField(blank=True, null=True)),
                ('actual_end_date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders_created_by', to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine')),
                ('processed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_orders_processed_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'İş Emirleri',
            },
        ),
    ]
