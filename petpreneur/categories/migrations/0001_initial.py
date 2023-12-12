# Generated by Django 4.2 on 2023-12-08 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        help_text="Максимальная длина - 150 символов",
                        max_length=150,
                        verbose_name="имя",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Максимальная длина - 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Subcategory",
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
                (
                    "name",
                    models.CharField(
                        help_text="Максимальная длина - 150 символов",
                        max_length=150,
                        verbose_name="имя",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Максимальная длина - 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="слаг",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategory",
                        to="categories.category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "подкатегория",
                "verbose_name_plural": "подкатегории",
            },
        ),
    ]