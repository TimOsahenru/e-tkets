# Generated by Django 5.1.6 on 2025-03-13 09:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("location", models.CharField(max_length=150)),
                ("location_tips", models.CharField(max_length=150)),
                ("call_for_direction", models.CharField(max_length=30)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("nigeria", "Nigeria"),
                            ("ghana", "Ghana"),
                            ("usa", "United States of America"),
                        ],
                        default="nigeria",
                        max_length=15,
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("chidren", "Children & Youth"),
                            ("fashion", "Fashion & Design"),
                            ("media", "Media & Gym"),
                            ("sport", "Sport & Fitness"),
                            ("government", "Government"),
                            ("community", "Community"),
                            ("charity", "Charity & Aid"),
                            ("school", "School & Education"),
                            ("career", "Career"),
                            ("spirituality", "Spirituality & Religion"),
                            ("investments", "Investments"),
                            ("business", "Business"),
                            ("technology", "Technology & Science"),
                            ("startups", "Startups & Small Business"),
                            ("foods", "Foods & Drink"),
                            ("art", "Art & Culture"),
                            ("music", "Music & Performance"),
                        ],
                        default="business",
                        max_length=50,
                    ),
                ),
                ("is_free", models.BooleanField(default=True)),
                (
                    "event_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
