# Generated by Django 5.1.3 on 2024-11-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0006_alter_todo_created_at_alter_todo_deadline_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(verbose_name="Data final"),
        ),
    ]
