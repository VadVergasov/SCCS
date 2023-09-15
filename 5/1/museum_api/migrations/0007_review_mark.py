# Generated by Django 4.2.5 on 2023-09-15 11:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("museum_api", "0006_review_alter_article_creation_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="mark",
            field=models.IntegerField(
                default=5,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
            preserve_default=False,
        ),
    ]
