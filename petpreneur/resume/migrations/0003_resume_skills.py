# Generated by Django 4.2 on 2023-12-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_skill_alter_category_name_alter_subcategory_name"),
        ("resume", "0002_alter_resume_category_alter_resume_subcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="skills",
            field=models.ManyToManyField(
                help_text="выберите свои навыки",
                related_name="resume",
                to="categories.skill",
                verbose_name="навыки",
            ),
        ),
    ]