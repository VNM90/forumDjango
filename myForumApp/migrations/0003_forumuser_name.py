# Generated by Django 3.2.2 on 2021-06-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myForumApp', '0002_forumuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumuser',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]