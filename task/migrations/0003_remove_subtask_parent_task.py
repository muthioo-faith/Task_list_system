# Generated by Django 3.2.12 on 2023-05-31 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20230531_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='parent_task',
        ),
    ]
