# Generated by Django 5.2.1 on 2025-06-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovinos', '0004_rename_consumo_refeicao_peso_racao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refeicao',
            name='horario_entrada',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
