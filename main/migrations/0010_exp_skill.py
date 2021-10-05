# Generated by Django 3.2.5 on 2021-08-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210817_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('startdate', models.IntegerField()),
                ('enddate', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('rate', models.PositiveSmallIntegerField(max_length=3)),
            ],
        ),
    ]
