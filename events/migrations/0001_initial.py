# Generated by Django 4.0.2 on 2022-02-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=1000)),
                ('language', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
    ]
