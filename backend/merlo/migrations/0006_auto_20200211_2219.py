# Generated by Django 3.0.3 on 2020-02-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlo', '0005_auto_20200211_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
