# Generated by Django 3.2.25 on 2024-09-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("redis_modules", "0002_auto_20240827_1912"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbredismodulesupport",
            name="so_file",
            field=models.CharField(default="", max_length=64, verbose_name="so文件名"),
        ),
    ]
