# Generated by Django 5.0.1 on 2024-01-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturisicos',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
