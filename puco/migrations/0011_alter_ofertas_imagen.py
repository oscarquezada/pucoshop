# Generated by Django 3.2.3 on 2021-07-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0010_ofertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
