# Generated by Django 5.1.7 on 2025-03-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.TextField()),
                ('url', models.TextField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
