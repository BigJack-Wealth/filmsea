# Generated by Django 4.0.3 on 2022-04-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_rename_videodetail_videod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videod',
            name='videod',
            field=models.FileField(upload_to='movie/%y'),
        ),
    ]
