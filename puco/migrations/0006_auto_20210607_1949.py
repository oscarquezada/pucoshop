# Generated by Django 3.2.3 on 2021-06-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0005_cliente_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
