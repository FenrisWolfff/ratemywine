# Generated by Django 4.2.11 on 2024-05-29 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_rating_user_delete_userinformation"),
    ]

    operations = [
        migrations.DeleteModel(name="UserLogIn",),
    ]
