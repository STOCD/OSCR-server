# Generated by Django 4.2.9 on 2024-02-12 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("combatlog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="metadata",
            name="damage_chart",
        ),
        migrations.RemoveField(
            model_name="metadata",
            name="dps_chart",
        ),
        migrations.RemoveField(
            model_name="metadata",
            name="npc_damage_chart",
        ),
        migrations.RemoveField(
            model_name="metadata",
            name="npc_dps_chart",
        ),
    ]
