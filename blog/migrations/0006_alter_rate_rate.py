# Generated by Django 4.1.4 on 2023-02-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rate_rate_rate value is valid between 1 and 5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(default=5),
        ),
    ]
