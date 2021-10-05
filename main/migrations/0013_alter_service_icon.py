# Generated by Django 3.2.5 on 2021-08-17 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
    ]
