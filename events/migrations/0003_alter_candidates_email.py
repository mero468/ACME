# Generated by Django 4.0.2 on 2022-02-25 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_candidates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
