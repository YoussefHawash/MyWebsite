# Generated by Django 3.2.5 on 2021-08-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210818_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git',
            field=models.URLField(blank=True),
        ),
    ]
