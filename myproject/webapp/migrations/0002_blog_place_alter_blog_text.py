# Generated by Django 4.1.1 on 2023-06-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='place',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=150),
        ),
    ]
