# Generated by Django 3.0.3 on 2020-02-11 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merlo', '0003_auto_20200211_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.TextField(default='')),
                ('email', models.SlugField(default='', unique=True)),
                ('avatar', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merlo.User'),
        ),
    ]
