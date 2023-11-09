# Generated by Django 4.2.5 on 2023-11-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("museum_api", "0007_review_mark"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("count", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]