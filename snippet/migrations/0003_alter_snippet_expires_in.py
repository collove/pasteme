# Generated by Django 4.0.6 on 2022-08-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippet", "0002_snippet_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="snippet",
            name="expires_in",
            field=models.SmallIntegerField(
                choices=[(1, "One Day"), (7, "One Week"), (30, "One Month")],
                default=7,
                verbose_name="Expires in",
            ),
        ),
    ]
