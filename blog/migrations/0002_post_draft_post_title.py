# Generated by Django 5.2.1 on 2025-06-06 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Post title', max_length=80),
            preserve_default=False,
        ),
    ]
