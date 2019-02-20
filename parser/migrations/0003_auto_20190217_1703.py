# Generated by Django 2.1.7 on 2019-02-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='categoryId',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
