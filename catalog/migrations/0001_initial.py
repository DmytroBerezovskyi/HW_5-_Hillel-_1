# Generated by Django 4.2.2 on 2023-07-21 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(help_text="Enter a city", max_length=200)),
                ("state", models.CharField(help_text="Enter a state", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                ("exp_date", models.DateField(blank=True, null=True)),
                ("vendor_code", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "city",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="catalog.city",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalog.city",
                    ),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        help_text="Select a product", to="catalog.product"
                    ),
                ),
            ],
        ),
    ]
