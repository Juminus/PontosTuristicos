# Generated by Django 4.2.5 on 2024-01-13 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('pontos_turisticos', '0005_pontosturisicos_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisicos',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
            preserve_default=False,
        ),
    ]
