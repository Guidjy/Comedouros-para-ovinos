from django.db import migrations, models
from datetime import date

class Migration(migrations.Migration):

    dependencies = [
        ('ovinos', '0003_alter_refeicao_comportamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refeicao',
            old_name='consumo',
            new_name='peso_racao',
        ),
        migrations.RemoveField(
            model_name='refeicao',
            name='dia_horario',
        ),
        migrations.AddField(
            model_name='refeicao',
            name='dia',
            field=models.DateField(default=date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refeicao',
            name='peso_na_entrada',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='refeicao',
            name='horario_entrada',
            field=models.TimeField(),
        ),
    ]
