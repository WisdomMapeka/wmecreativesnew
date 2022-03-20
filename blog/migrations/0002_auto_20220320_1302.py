# Generated by Django 3.0 on 2022-03-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]
