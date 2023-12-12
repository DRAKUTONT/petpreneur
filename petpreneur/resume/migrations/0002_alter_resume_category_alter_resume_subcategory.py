# Generated by Django 4.2 on 2023-12-11 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_skill_alter_category_name_alter_subcategory_name"),
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="resume",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="categories.subcategory",
            ),
        ),
    ]