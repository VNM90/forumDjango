# Generated by Django 3.2.2 on 2021-06-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myForumApp', '0004_remove_forumuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumuser',
            name='name',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
