# Generated by Django 3.1.4 on 2021-01-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_auto_20201207_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='Completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='score',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]