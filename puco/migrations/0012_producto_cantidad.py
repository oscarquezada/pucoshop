# Generated by Django 3.2.3 on 2021-07-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0011_alter_ofertas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]