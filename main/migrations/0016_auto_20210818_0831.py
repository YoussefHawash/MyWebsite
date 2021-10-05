# Generated by Django 3.2.5 on 2021-08-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210817_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='creator',
            name='firstaboutline',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='creator',
            name='secondaboutline',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.FileField(upload_to='icons/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rate',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
