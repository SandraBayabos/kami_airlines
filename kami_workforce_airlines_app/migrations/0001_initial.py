# Generated by Django 5.0 on 2023-12-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('airplane_id', models.AutoField(primary_key=True, serialize=False)),
                ('passenger_count', models.IntegerField()),
            ],
        ),
    ]
