# Generated by Django 3.2.3 on 2021-06-17 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0008_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(max_length=10),
        ),
    ]
