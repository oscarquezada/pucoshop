# Generated by Django 3.2.3 on 2021-06-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0004_auto_20210605_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='clave',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
