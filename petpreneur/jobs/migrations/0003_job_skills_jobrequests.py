# Generated by Django 4.2 on 2023-12-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_skill_alter_category_name_alter_subcategory_name"),
        ("resume", "0004_remove_resume_skills"),
        ("jobs", "0002_alter_job_category_alter_job_subcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="skills",
            field=models.ManyToManyField(
                related_name="job", to="categories.skill", verbose_name="навыки"
            ),
        ),
        migrations.CreateModel(
            name="JobRequests",
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
                    "text",
                    models.TextField(help_text="Введите текст", verbose_name="текст"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Это поле создается автоматически",
                        verbose_name="дата и время создания",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Отправлено"), (2, "Одобрено"), (3, "Отклонено")],
                        verbose_name="статус",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_requests",
                        to="jobs.job",
                        verbose_name="работа",
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_requests",
                        to="resume.resume",
                        verbose_name="резюме",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]