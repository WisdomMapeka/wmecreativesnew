# Generated by Django 3.0 on 2023-07-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20230708_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author_image_atlt_text',
            field=models.CharField(blank=True, help_text='alt text of an image', max_length=1000, null=True),
        ),
    ]
