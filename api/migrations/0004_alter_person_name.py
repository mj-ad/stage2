# Generated by Django 4.2.5 on 2023-09-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_person_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="name",
            field=models.CharField(max_length=256, null=True),
        ),
    ]