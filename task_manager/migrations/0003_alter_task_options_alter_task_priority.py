# Generated by Django 4.1.7 on 2023-02-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_alter_worker_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_completed']},
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Urgent', 'Urgent Priority'), ('High', 'High Priority'), ('Medium', 'Medium Priority'), ('Low', 'Low Priority')], default='Medium', max_length=6),
        ),
    ]