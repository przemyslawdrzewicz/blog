# Generated by Django 3.0.2 on 2020-01-20 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_article_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='edit',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
