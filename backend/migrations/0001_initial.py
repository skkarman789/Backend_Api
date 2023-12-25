# Generated by Django 5.0 on 2023-12-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('is_overspeeding', models.BooleanField(default=False)),
                ('vehicle_no', models.CharField(max_length=255)),
                ('location_type', models.TextField(max_length=255)),
            ],
        ),
    ]