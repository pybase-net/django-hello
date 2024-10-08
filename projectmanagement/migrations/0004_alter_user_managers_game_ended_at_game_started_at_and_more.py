# Generated by Django 5.0.7 on 2024-07-22 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0003_auto_20240715_0902'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='ended_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='projectmanagement.question'),
        ),
    ]
