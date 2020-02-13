# Generated by Django 3.0.3 on 2020-02-13 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merlo', '0007_article_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merlo.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='version',
            field=models.IntegerField(default=1, null=True),
        ),
    ]