# Generated by Django 2.1.7 on 2019-03-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0004_locale'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
