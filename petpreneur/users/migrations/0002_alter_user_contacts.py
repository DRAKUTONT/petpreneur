# Generated by Django 4.2 on 2023-12-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="contacts",
            field=models.TextField(blank=True, null=True, verbose_name="контакты"),
        ),
    ]
