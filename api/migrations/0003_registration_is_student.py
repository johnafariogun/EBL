# Generated by Django 4.1.1 on 2023-06-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_registration_faculty_alter_registration_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="is_student",
            field=models.CharField(
                choices=[("1", "Yes"), ("0", "No")], default="Yes", max_length=4
            ),
        ),
    ]
