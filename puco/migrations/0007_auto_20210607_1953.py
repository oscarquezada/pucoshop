# Generated by Django 3.2.3 on 2021-06-07 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0006_auto_20210607_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='is_superuser',
        ),
    ]