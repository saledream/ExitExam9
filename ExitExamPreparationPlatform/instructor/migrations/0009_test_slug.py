# Generated by Django 5.0.3 on 2024-03-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0008_test_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
