# Generated by Django 3.0.3 on 2020-02-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
