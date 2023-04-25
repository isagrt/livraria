# Generated by Django 4.1.7 on 2023-03-24 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0003_autor"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
        migrations.CreateModel(
            name="Livro",
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
                ("titulo", models.CharField(max_length=255)),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=7, null=True
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="livraria.categoria",
                    ),
                ),
                (
                    "editora",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="livraria.editora",
                    ),
                ),
            ],
        ),
    ]
