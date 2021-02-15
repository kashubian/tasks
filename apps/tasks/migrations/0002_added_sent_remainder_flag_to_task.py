# Generated by Django 3.1.6 on 2021-02-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_added_task_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='task',
            name='sent_remainder',
            field=models.BooleanField(default=False),
        ),
    ]