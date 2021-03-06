# Generated by Django 3.2.3 on 2021-06-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puco', '0002_rename_cliente_cliente2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Cliente2',
        ),
    ]
