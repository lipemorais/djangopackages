# Generated by Django 2.2.24 on 2021-09-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_auto_20210906_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
    ]
