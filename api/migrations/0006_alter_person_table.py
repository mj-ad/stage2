# Generated by Django 4.2.5 on 2023-09-14 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_person_name"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="person",
            table="person",
        ),
    ]
