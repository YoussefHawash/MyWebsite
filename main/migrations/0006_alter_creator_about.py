# Generated by Django 3.2.5 on 2021-08-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210817_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='about',
            field=models.CharField(max_length=300),
        ),
    ]
