# Generated by Django 4.2.9 on 2024-02-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("combatlog", "0002_remove_metadata_damage_chart_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="combatlog",
            name="file",
        ),
        migrations.AddField(
            model_name="combatlog",
            name="data",
            field=models.BinaryField(default=None, null=True),
        ),
    ]
