# Generated by Django 2.2.28 on 2023-12-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_hide',
            field=models.BooleanField(default=False),
        ),
    ]