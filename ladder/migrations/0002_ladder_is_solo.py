# Generated by Django 4.2.9 on 2024-02-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ladder", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ladder",
            name="is_solo",
            field=models.BooleanField(default=False),
        ),
    ]
