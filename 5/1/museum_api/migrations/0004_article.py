# Generated by Django 4.2.5 on 2023-09-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("museum_api", "0003_tour"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("creation_time", models.TimeField(auto_created=True)),
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("content", models.TextField()),
            ],
        ),
    ]
