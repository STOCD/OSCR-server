# Generated by Django 4.2.9 on 2024-04-13 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("combatlog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ladder",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("difficulty", models.TextField(default=None, null=True)),
                ("is_solo", models.BooleanField(default=False)),
                ("is_space", models.BooleanField(default=True)),
                ("metric", models.TextField()),
                ("internal_name", models.TextField()),
                ("internal_difficulty", models.TextField(default=None, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Variant",
            fields=[
                ("name", models.TextField(primary_key=True, serialize=False)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("is_ground_variant", models.BooleanField(default=True)),
                ("is_space_variant", models.BooleanField(default=True)),
                (
                    "exclude_ground",
                    models.ManyToManyField(
                        blank=True,
                        related_name="exclude_ground_variant_set",
                        to="ladder.variant",
                    ),
                ),
                (
                    "exclude_space",
                    models.ManyToManyField(
                        blank=True,
                        related_name="exclude_space_variant_set",
                        to="ladder.variant",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LadderEntry",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("player", models.TextField()),
                ("data", models.JSONField()),
                (
                    "combatlog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="combatlog.combatlog",
                    ),
                ),
                (
                    "ladder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ladder.ladder"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="ladder",
            name="variant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ladder.variant"
            ),
        ),
    ]
