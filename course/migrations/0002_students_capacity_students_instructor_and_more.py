# Generated by Django 5.0 on 2023-12-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='capacity',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='students',
            name='instructor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='open_seats',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='students',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
