# Generated by Django 5.0.6 on 2024-05-22 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.CharField(max_length=50)),
                ('qualidades', models.CharField(max_length=50)),
                ('funcionalidades', models.CharField(max_length=50)),
                ('desing', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
    ]
