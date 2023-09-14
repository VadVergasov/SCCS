# Generated by Django 4.2.5 on 2023-09-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("museum_api", "0005_article_id_alter_article_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=60)),
                ("content", models.TextField()),
                ("creation_time", models.TimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="article",
            name="creation_time",
            field=models.TimeField(auto_now=True),
        ),
    ]