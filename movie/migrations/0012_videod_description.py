# Generated by Django 4.0.3 on 2022-04-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_videod_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='videod',
            name='description',
            field=models.TextField(default=True, max_length=1000),
        ),
    ]
